# Job-Ready Testing Portfolio Project

This project is designed to match junior `Test Automation` / `System Test` roles quickly.
It demonstrates:

- Python coding
- API testing with `pytest`
- SQL validation with `sqlite3`
- Negative and edge-case testing
- Furhat-style conversation scenario testing
- Bug-report style documentation
- CI with GitHub Actions

## Project Structure

- `src/api_client.py` - simple API client to test HTTP behavior
- `src/db.py` - SQLite test-results store and query helpers
- `src/furhat_simulator.py` - local Furhat-style conversation engine
- `src/furhat_api_client.py` - real Furhat websocket client
- `tests/test_api.py` - API and negative-path tests with mocking
- `tests/test_db.py` - SQL-based validation tests
- `tests/test_furhat_simulator.py` - greeting/fallback/interruption/latency tests
- `tests/test_furhat_api_client.py` - realtime websocket contract + optional live smoke test
- `docs/bug_report_template.md` - interview-ready QA artifact
- `.github/workflows/tests.yml` - automated test pipeline

## Quick Start

1. Create and activate a virtual environment
2. Install dependencies
3. Run tests

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Skills You Can Claim From This Project

- Designed test scenarios and negative-path checks
- Wrote API tests using `pytest` and mocking
- Validated data integrity with SQL queries
- Produced reproducible bug report templates
- Automated regression tests in CI
- Tested conversational robot behavior via scenario-based validation

## Furhat-Style Scenarios Covered

- greeting intent detection
- unknown-intent fallback behavior
- interruption recovery behavior
- response latency threshold check

## Real Furhat API Testing (Realtime)

This repo now includes a Furhat realtime websocket client with optional live smoke test.

### 1) Configure local env

Copy `.env.example` values into your shell:

```powershell
$env:FURHAT_WS_URL="ws://192.168.1.108:9000/v1/events"
$env:FURHAT_API_KEY="LEO"
```

In WSL/Linux:

```bash
export FURHAT_WS_URL="ws://192.168.1.108:9000/v1/events"
export FURHAT_API_KEY="LEO"
```

### 2) Run full tests

```bash
python -m pytest -q
```

The live Furhat test auto-skips until both env vars are provided.

## Suggested Next Furhat Upgrade

Replace the local simulator with your real endpoint wrapper and add:

- intent/fallback test scenarios
- response-latency thresholds
- turn-taking interruption tests
