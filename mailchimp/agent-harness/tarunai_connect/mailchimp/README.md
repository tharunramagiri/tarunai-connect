# tarunai-connect-mailchimp

Python CLI harness for the [Mailchimp Marketing API v3.0](https://mailchimp.com/developer/marketing/docs/fundamentals/), built on the [tarunAI Connect](https://github.com/tharunramagiri/tarunai-connect) framework.

## Install

```bash
pip install git+https://github.com/tharunramagiri/tarunai-connect.git#subdirectory=mailchimp/agent-harness
```

## Auth

```bash
export MAILCHIMP_API_KEY=<your-api-key>-<datacenter>
```

## Usage

```bash
tarunai-connect-mailchimp ping
tarunai-connect-mailchimp --json lists list
tarunai-connect-mailchimp --json campaigns list --count 10
tarunai-connect-mailchimp                  # interactive REPL
```

See `SKILL.md` for full command reference.
