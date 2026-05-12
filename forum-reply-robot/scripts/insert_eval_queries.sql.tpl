-- Query 集插入模板
-- 用法:填充下方 VALUES 列表,然后执行:
--   python scripts/db_shell.py sql "$(cat scripts/insert_eval_queries.sql.tpl)"
-- 或用任意 DB 客户端直接跑
--
-- 字段说明:
--   query_id        业务 ID,字符串主键,建议 Q001/Q002 递增
--   question        用户原始问题(拼接后的 title + body 也可)
--   expected_output 可留空;若想启用 Contextual Precision/Recall 则填标准答案
--   note            备注,例如"社区元话题 / 技术问题 / FAQ"

INSERT INTO eval_query_set (query_id, question, expected_output, note) VALUES
    ('Q001', '替换为第 1 条查询', NULL, '替换为分类备注')
    -- , ('Q002', '替换为第 2 条查询', NULL, NULL)
    -- , ('Q003', '替换为第 3 条查询', NULL, NULL)
    -- , ('Q004', '替换为第 4 条查询', NULL, NULL)
    -- , ('Q005', '替换为第 5 条查询', NULL, NULL)
    -- , ('Q006', '替换为第 6 条查询', NULL, NULL)
    -- , ('Q007', '替换为第 7 条查询', NULL, NULL)
    -- , ('Q008', '替换为第 8 条查询', NULL, NULL)
    -- , ('Q009', '替换为第 9 条查询', NULL, NULL)
    -- , ('Q010', '替换为第 10 条查询', NULL, NULL)
ON CONFLICT (query_id) DO UPDATE SET
    question        = EXCLUDED.question,
    expected_output = EXCLUDED.expected_output,
    note            = EXCLUDED.note;
