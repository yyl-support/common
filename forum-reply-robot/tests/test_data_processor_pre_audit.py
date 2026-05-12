from unittest.mock import Mock

import pytest

from src.ForumBot import data_processor as data_processor_module
from src.ForumBot.data_processor import DataProcessor, fetch_all_forum_topics, parse_pre_audit_readiness


@pytest.fixture
def config():
    return {
        "api": {"base_url": "https://api.example.com", "api_key": "dummy-key"},
        "image_processing": {"model1": "model-a", "model2": "model-b", "model3": "model-c", "base_url": "https://images.example.com"},
        "database": {"host": "localhost", "port": 5432, "database": "forum", "user": "tester", "password": "secret", "sslmode": "disable"},
        "pre_audit": {"readiness_field": "是否准备好AI预审（必选）", "readiness_yes_value": "是"},
    }


def test_parse_pre_audit_readiness_from_table(config):
    html = "<table><tr><td>是否准备好AI预审（必选）</td><td>是</td></tr></table>"
    assert parse_pre_audit_readiness(html, config) is True


def test_load_pre_audit_existing_data_returns_id_map(config, monkeypatch):
    processor, cursor, conn, close_mock = DataProcessor(config), Mock(), Mock(), Mock()
    cursor.fetchall.return_value = [(101,), (202,)]
    conn.cursor.return_value = cursor
    monkeypatch.setattr(processor, "_get_db_connection", lambda: conn)
    monkeypatch.setattr(processor, "_close_db_connection", close_mock)
    assert processor.load_pre_audit_existing_data() == {101: True, 202: True}
    cursor.execute.assert_called_once_with("SELECT id FROM pre_audit_topics")
    close_mock.assert_called_once_with(conn)


def test_append_to_db_accepts_pre_audit_table(config, monkeypatch):
    processor, cursor, conn, captured = DataProcessor(config), Mock(), Mock(), {}
    conn.cursor.return_value = cursor
    monkeypatch.setattr(processor, "_get_db_connection", lambda: conn)
    monkeypatch.setattr(processor, "_close_db_connection", lambda connection: None)
    monkeypatch.setattr(data_processor_module, "execute_values", lambda cursor_obj, query, rows: captured.update(query=query, rows=rows))
    payload = [{"id": 1, "title": "topic", "user_question": "question", "best_answer": "answer", "tags": [{"name": "pre-audit"}], "replies": [{"id": 2}], "created_at": "2026-04-16T00:00:00Z", "llm_answer": "done", "summary_question": "summary"}]
    assert processor.append_to_db(payload, "pre_audit_topics") is True
    assert "INSERT INTO pre_audit_topics" in captured["query"]
    assert captured["rows"][0][0] == 1 and captured["rows"][0][4] == "pre-audit"
    conn.commit.assert_called_once()


def test_append_to_db_rejects_invalid_table(config):
    with pytest.raises(ValueError, match="Invalid table name"):
        DataProcessor(config).append_to_db([{"id": 1}], "bad_table")


@pytest.mark.parametrize(("html", "expected"), [("", None), ("<div>是否准备好AI预审：是</div>", True), ("<div>nothing relevant</div>", None)])
def test_parse_pre_audit_readiness_extra_cases(config, html, expected):
    assert parse_pre_audit_readiness(html, config) is expected


def test_parse_pre_audit_readiness_returns_none_on_parser_error(config, monkeypatch):
    monkeypatch.setattr(data_processor_module, "BeautifulSoup", lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("boom")))
    assert parse_pre_audit_readiness("<div>ignored</div>", config) is None


def test_fetch_all_forum_topics_uses_custom_pre_audit_keys(monkeypatch):
    config = {"forum": {"base_url": "https://forum.example.com", "verify_ssl": False, "request_delay": 0}, "monitor": {"pre_audit_tag": ["pre-audit"], "pre_audit_cutoff_date": "2026-01-01", "pre_audit_category_path": ["/c/pre-audit"]}}
    responses, urls = [{"topic_list": {"topics": [{"id": 1, "tags": ["pre-audit"], "created_at": "2026-04-16T00:00:00.000Z"}, {"id": 2, "tags": ["general"], "created_at": "2026-04-16T00:00:00.000Z"}]}}, {"topic_list": {"topics": []}}], []

    class FakeResponse:
        def __init__(self, payload): self._payload = payload
        def raise_for_status(self): return None
        def json(self): return self._payload

    monkeypatch.setattr(data_processor_module.requests, "get", lambda url, **kwargs: (urls.append(url), FakeResponse(responses.pop(0)))[1])
    monkeypatch.setattr(data_processor_module.time, "sleep", lambda _: None)
    result = fetch_all_forum_topics(config, tag_key="pre_audit_tag", cutoff_date_key="pre_audit_cutoff_date", category_path_key="pre_audit_category_path")
    assert [topic["id"] for topic in result] == [1]
    assert urls[0].endswith("/c/pre-audit.json")


def test_create_tables_creates_pre_audit_tables(config, monkeypatch):
    processor, cursor, conn = DataProcessor(config), Mock(), Mock()
    conn.cursor.return_value = cursor
    monkeypatch.setattr(processor, "_get_db_connection", lambda: conn)
    monkeypatch.setattr(processor, "_close_db_connection", lambda connection: None)
    processor.create_tables()
    executed_sql = "\n".join(call.args[0] for call in cursor.execute.call_args_list)
    assert "CREATE TABLE IF NOT EXISTS pre_audit_topics" in executed_sql
    assert "CREATE TABLE IF NOT EXISTS pre_audit_processed_topics" in executed_sql
