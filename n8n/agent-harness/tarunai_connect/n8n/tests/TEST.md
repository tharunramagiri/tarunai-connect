# Testing tarunai-connect-n8n

## Unit tests (no n8n required)

```bash
cd agent-harness
pip install -e .
pytest tarunai_connect/n8n/tests/test_core.py -v
```

## E2E tests (n8n instance required)

```bash
export N8N_BASE_URL=https://your-n8n-instance.com
export N8N_API_KEY=your-api-key
pytest tarunai_connect/n8n/tests/test_full_e2e.py -v -m e2e
```

## Run all tests

```bash
pytest tarunai_connect/n8n/tests/ -v
```

## Skip E2E

```bash
pytest tarunai_connect/n8n/tests/ -v -m "not e2e"
```
