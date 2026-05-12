"""
CSV 数据迁移到 PostgreSQL 数据库脚本

使用方法：
    1. 确保 PostgreSQL 已安装并创建了数据库
    2. 修改 config/config.yaml 中的 storage.backend 为 'database'
    3. 运行：python migrate_csv_to_db.py

注意：
    - 此脚本会先清空目标表再导入数据
    - 建议在运行前备份数据库
"""

import csv
import json
import sys
import os
from datetime import datetime
import psycopg2
from psycopg2.extras import Json, execute_values

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.utils import load_config
from src.ForumBot.logging_config import main_logger as logger


CSV_TABLE_MAPPING = {
    'forum_topics': {
        'csv_key': 'csv_file',
        'table': 'forum_topics',
        'fields': ['id', 'title', 'user_question', 'best_answer', 'tags', 'replies', 'created_at', 'llm_answer', 'summary_question']
    },
    'processed_forum_topics': {
        'csv_key': 'processed_csv_file',
        'table': 'processed_forum_topics',
        'fields': ['id', 'title', 'user_question', 'best_answer', 'tags', 'replies', 'created_at', 'llm_answer', 'summary_question']
    },
    'pre_audit_topics': {
        'csv_key': 'pre_audit_csv_file',
        'table': 'pre_audit_topics',
        'fields': ['id', 'title', 'user_question', 'best_answer', 'tags', 'replies', 'created_at', 'llm_answer', 'summary_question']
    },
    'pre_audit_processed_topics': {
        'csv_key': 'pre_audit_processed_csv_file',
        'table': 'pre_audit_processed_topics',
        'fields': ['id', 'title', 'user_question', 'best_answer', 'tags', 'replies', 'created_at', 'llm_answer', 'summary_question']
    },
    'forum_search_results': {
        'csv_key': 'search_results_csv_file',
        'table': 'forum_search_results',
        'fields': ['topic_id', 'search_keyword', 'search_timestamp', 'total_results', 'displayed_results',
                   'result_1', 'result_2', 'result_3', 'result_4', 'result_5',
                   'result_6', 'result_7', 'result_8', 'result_9', 'result_10']
    },
    'forum_retrieval_results': {
        'csv_key': 'retrieval_results_csv_file',
        'table': 'forum_retrieval_results',
        'fields': ['topic_id', 'related_docs', 'created_at']
    },
    'consume_tokens_topic': {
        'csv_key': 'token_usage_csv_file',
        'table': 'consume_tokens_topic',
        'fields': ['topic_id', 'prompt_tokens', 'completion_tokens', 'total_tokens', 'model_calls', 'created_at']
    }
}


def get_db_connection(config):
    """获取数据库连接"""
    db_params = {
        'host': config['database']['host'],
        'port': config['database']['port'],
        'database': config['database']['database'],
        'user': config['database']['user'],
        'password': config['database']['password'],
        'sslmode': config['database'].get('sslmode', 'disable')
    }
    return psycopg2.connect(**db_params)


def parse_json_field(value):
    """解析JSON字段"""
    if not value or value == '':
        return None
    try:
        if isinstance(value, str):
            return Json(json.loads(value))
        return Json(value)
    except (json.JSONDecodeError, TypeError):
        return value


def parse_timestamp(value):
    """解析时间戳字段"""
    if not value or value == '':
        return None
    try:
        if isinstance(value, str):
            for fmt in ['%Y-%m-%dT%H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M:%S']:
                try:
                    return datetime.strptime(value.replace('+00:00', '').replace('Z', ''), fmt)
                except ValueError:
                    continue
        return value
    except Exception:
        return value


def clear_table(conn, table_name):
    """清空表数据"""
    try:
        cursor = conn.cursor()
        cursor.execute(f"TRUNCATE TABLE {table_name} CASCADE")
        conn.commit()
        cursor.close()
        logger.info(f"已清空表: {table_name}")
        return True
    except Exception as e:
        logger.error(f"清空表 {table_name} 时出错: {e}")
        conn.rollback()
        return False


def migrate_topics_table(conn, csv_path, table_name, fields):
    """迁移主题类表数据"""
    if not os.path.exists(csv_path):
        logger.warning(f"CSV文件不存在，跳过: {csv_path}")
        return 0

    rows = []
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            replies_value = parse_json_field(row.get('replies', ''))
            created_at_value = parse_timestamp(row.get('created_at', ''))

            rows.append((
                int(row['id']) if row.get('id') else None,
                row.get('title', ''),
                row.get('user_question', ''),
                row.get('best_answer', ''),
                row.get('tags', ''),
                replies_value,
                created_at_value,
                row.get('llm_answer', ''),
                row.get('summary_question', '')
            ))

    if not rows:
        logger.info(f"CSV文件为空: {csv_path}")
        return 0

    deduped = {}
    for row in rows:
        key = row[0]
        if key is None:
            continue
        deduped[key] = row
    dropped = len(rows) - len(deduped)
    if dropped > 0:
        logger.info(f"CSV {csv_path} 存在 {dropped} 条重复 id，保留最后一条")
    rows = list(deduped.values())

    cursor = conn.cursor()
    insert_query = f"""
        INSERT INTO {table_name}
        (id, title, user_question, best_answer, tags, replies, created_at, llm_answer, summary_question)
        VALUES %s
        ON CONFLICT (id) DO UPDATE SET
            title = EXCLUDED.title,
            user_question = EXCLUDED.user_question,
            best_answer = EXCLUDED.best_answer,
            tags = EXCLUDED.tags,
            replies = EXCLUDED.replies,
            created_at = EXCLUDED.created_at,
            llm_answer = EXCLUDED.llm_answer,
            summary_question = EXCLUDED.summary_question
    """
    
    execute_values(cursor, insert_query, rows)
    conn.commit()
    cursor.close()
    logger.info(f"成功迁移 {len(rows)} 条数据到 {table_name}")
    return len(rows)


def migrate_search_results(conn, csv_path, table_name):
    """迁移搜索结果表数据"""
    if not os.path.exists(csv_path):
        logger.warning(f"CSV文件不存在，跳过: {csv_path}")
        return 0

    rows = []
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result_columns = []
            for i in range(1, 11):
                result_columns.append(parse_json_field(row.get(f'result_{i}', '')))
            
            rows.append((
                int(row['topic_id']) if row.get('topic_id') else None,
                row.get('search_keyword', ''),
                parse_timestamp(row.get('search_timestamp', '')),
                int(row['total_results']) if row.get('total_results') else 0,
                int(row['displayed_results']) if row.get('displayed_results') else 0,
                *result_columns
            ))

    if not rows:
        logger.info(f"CSV文件为空: {csv_path}")
        return 0

    cursor = conn.cursor()
    insert_query = f"""
        INSERT INTO {table_name}
        (topic_id, search_keyword, search_timestamp, total_results, displayed_results,
         result_1, result_2, result_3, result_4, result_5,
         result_6, result_7, result_8, result_9, result_10)
        VALUES %s
    """
    
    execute_values(cursor, insert_query, rows)
    conn.commit()
    cursor.close()
    logger.info(f"成功迁移 {len(rows)} 条数据到 {table_name}")
    return len(rows)


def migrate_retrieval_results(conn, csv_path, table_name):
    """迁移检索结果表数据"""
    if not os.path.exists(csv_path):
        logger.warning(f"CSV文件不存在，跳过: {csv_path}")
        return 0

    rows = []
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((
                int(row['topic_id']) if row.get('topic_id') else None,
                row.get('related_docs', ''),
                parse_timestamp(row.get('created_at', ''))
            ))

    if not rows:
        logger.info(f"CSV文件为空: {csv_path}")
        return 0

    cursor = conn.cursor()
    insert_query = f"""
        INSERT INTO {table_name}
        (topic_id, related_docs, created_at)
        VALUES %s
    """
    
    execute_values(cursor, insert_query, rows)
    conn.commit()
    cursor.close()
    logger.info(f"成功迁移 {len(rows)} 条数据到 {table_name}")
    return len(rows)


def migrate_token_usage(conn, csv_path, table_name):
    """迁移token使用量表数据"""
    if not os.path.exists(csv_path):
        logger.warning(f"CSV文件不存在，跳过: {csv_path}")
        return 0

    rows = []
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((
                int(row['topic_id']) if row.get('topic_id') else None,
                int(row['prompt_tokens']) if row.get('prompt_tokens') else 0,
                int(row['completion_tokens']) if row.get('completion_tokens') else 0,
                int(row['total_tokens']) if row.get('total_tokens') else 0,
                int(row['model_calls']) if row.get('model_calls') else 0,
                parse_timestamp(row.get('created_at', ''))
            ))

    if not rows:
        logger.info(f"CSV文件为空: {csv_path}")
        return 0

    deduped = {}
    for row in rows:
        key = row[0]
        if key is None:
            continue
        deduped[key] = row
    dropped = len(rows) - len(deduped)
    if dropped > 0:
        logger.info(f"CSV {csv_path} 存在 {dropped} 条重复 topic_id，保留最后一条")
    rows = list(deduped.values())

    cursor = conn.cursor()
    insert_query = f"""
        INSERT INTO {table_name}
        (topic_id, prompt_tokens, completion_tokens, total_tokens, model_calls, created_at)
        VALUES %s
        ON CONFLICT (topic_id) DO UPDATE SET
            prompt_tokens = EXCLUDED.prompt_tokens,
            completion_tokens = EXCLUDED.completion_tokens,
            total_tokens = EXCLUDED.total_tokens,
            model_calls = EXCLUDED.model_calls,
            created_at = EXCLUDED.created_at
    """
    
    execute_values(cursor, insert_query, rows)
    conn.commit()
    cursor.close()
    logger.info(f"成功迁移 {len(rows)} 条数据到 {table_name}")
    return len(rows)


def main():
    """主迁移函数"""
    logger.info("=" * 60)
    logger.info("CSV 数据迁移到 PostgreSQL 数据库")
    logger.info("=" * 60)

    config = load_config()
    
    storage_backend = config.get('storage', {}).get('backend', 'database')
    if storage_backend != 'database':
        logger.error(f"当前存储后端为 '{storage_backend}'，请先修改 config.yaml 中的 storage.backend 为 'database'")
        return False

    try:
        conn = get_db_connection(config)
        logger.info("数据库连接成功")
    except Exception as e:
        logger.error(f"数据库连接失败: {e}")
        return False

    total_migrated = 0
    
    try:
        for name, mapping in CSV_TABLE_MAPPING.items():
            csv_key = mapping['csv_key']
            csv_path = config.get('paths', {}).get(csv_key)
            
            if not csv_path:
                logger.warning(f"未找到配置键 '{csv_key}'，跳过表 {name}")
                continue
            
            logger.info(f"\n处理表: {name}")
            logger.info(f"CSV路径: {csv_path}")
            
            if not clear_table(conn, mapping['table']):
                logger.error(f"清空表 {name} 失败，跳过")
                continue
            
            if name in ['forum_topics', 'processed_forum_topics', 'pre_audit_topics', 'pre_audit_processed_topics']:
                count = migrate_topics_table(conn, csv_path, mapping['table'], mapping['fields'])
            elif name == 'forum_search_results':
                count = migrate_search_results(conn, csv_path, mapping['table'])
            elif name == 'forum_retrieval_results':
                count = migrate_retrieval_results(conn, csv_path, mapping['table'])
            elif name == 'consume_tokens_topic':
                count = migrate_token_usage(conn, csv_path, mapping['table'])
            else:
                logger.warning(f"未知的表类型: {name}")
                continue
            
            total_migrated += count

        logger.info("\n" + "=" * 60)
        logger.info(f"迁移完成！总计迁移 {total_migrated} 条记录")
        logger.info("=" * 60)
        return True

    except Exception as e:
        logger.error(f"迁移过程中出错: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        conn.close()
        logger.info("数据库连接已关闭")


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)