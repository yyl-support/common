# AGENTS.md

## Quick Start (Local Windows)

```powershell
# Restore config if missing (deleted after each run for security)
Copy-Item config/config.yaml.startup-bak config/config.yaml

# Start service
$env:PYTHONPATH="."; $env:PYTHONIOENCODING="utf-8"
.venv/Scripts/python.exe main.py
```

Health check: `Invoke-RestMethod http://localhost:5000/health`

## Environment Requirements

- **Python**: 3.11 for Windows local (uses `netifaces-plus` wheel), 3.9 for Docker
- **SchemaFiles**: Must clone before first run:
  ```bash
  git clone https://gitcode.com/Richardli25/Redfish_SchemaFile.git src/ForumBot/SchemaValidation/SchemaFiles
  rm -rf src/ForumBot/SchemaValidation/SchemaFiles/.git
  ```
  (~7900 files, required for startup check at `main.py:check_schema_files()`)

## Config Security

`config/config.yaml` is **deleted after startup** (`main.py:delete_config_file()`). Always restore from backup:
```bash
cp config/config.yaml.startup-bak config/config.yaml
```

## Storage Backend

- `storage.backend: 'csv'` - Local mode, no PostgreSQL needed
- `storage.backend: 'database'` - Docker mode, requires PostgreSQL at configured host

When `backend: 'csv'`, `data_processor.create_tables()` returns early, skipping DB setup.

## Architecture

```
main.py
  ├── ForumMonitor (src/ForumBot/monitor.py) - 60s polling loop
  │     ├── _check_new_topics() → AI reply workflow
  │     └── _check_pre_audit_topics() → Redfish Schema validation
  ├── FullDataUpdate (src/update_lightrag/) - LightRAG initial sync
  └── UpdateLightRAGTimer - Daily incremental sync at UTC 18:00
```

External dependencies: LightRAG, Discourse forum API, SiliconFlow LLM, GitCode API, doc-search API.

## Testing

```bash
pytest tests/
```

`conftest.py` mocks: `psycopg2`, `langchain_openai`, `langchain_core`, `extract_reviews`. Tests can run without external services.

## Flask Endpoints

- `GET /health` → `{"status": "healthy"}`
- `GET /health/detail` → component status (monitor_instance, monitor_thread_alive, service_initialized)

Binding IP: `main.py:get_best_private_ip()` prefers `10.x` then `192.168.x`.

## Key Files

| File | Purpose |
|------|---------|
| `src/ForumBot/monitor.py` | Main polling loop, topic processing |
| `src/ForumBot/ai_processor.py` | LLM calls (injection check, summary, answer, quality) |
| `src/ForumBot/forum_client.py` | Forum API + LightRAG retrieval |
| `src/ForumBot/data_processor.py` | CSV/DB persistence |
| `src/update_lightrag/lightrag_client.py` | LightRAG HTTP client |
| `src/update_lightrag/full_data_init.py` | Full data sync to LightRAG |