# Test Guide — tarunai-connect-mailchimp

## Prerequisites

```bash
pip install -e ".[dev]"
# dev extras: pytest, pytest-cov, responses
```

## Unit tests (no API key needed)

```bash
cd mailchimp/agent-harness
pytest tarunai_connect/mailchimp/tests/test_core.py -v
```

Expected: all collected tests pass. Runtime < 5 seconds.

## Live E2E tests (requires MAILCHIMP_API_KEY)

```bash
export MAILCHIMP_API_KEY=<your-key>-<datacenter>
pytest tarunai_connect/mailchimp/tests/test_full_e2e.py -v -s
```

Expected: 9 tests. The fixture creates a throwaway audience, runs member and
merge-field operations against it, then deletes it. Runtime ~15–30 seconds.

Cleanup is automatic (the `test_list` fixture deletes the audience in a
`finally` block). If a run is interrupted, delete the `tarunai-connect-test-*`
list from your Mailchimp account manually.

## Coverage

```bash
pytest tarunai_connect/mailchimp/tests/test_core.py --cov=tarunai_connect.mailchimp.core --cov-report=term-missing
```

Target: ≥ 80% line coverage on `core/`.
