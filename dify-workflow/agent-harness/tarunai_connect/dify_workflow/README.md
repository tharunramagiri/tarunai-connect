# tarunai-connect-dify-workflow

tarunAI Connect wrapper for the open-source Dify workflow DSL editor.

This package does not reimplement the Dify workflow engine. It wraps the
existing `dify-workflow` CLI so agents can discover and use it through the
tarunAI Connect ecosystem and CLI-Hub.

## Install

Install the upstream Dify workflow CLI first:

```bash
python -m pip install "dify-ai-workflow-tools @ git+https://github.com/Akabane71/dify-workflow-cli.git@main"
```

Then install this harness:

```bash
pip install git+https://github.com/tharunramagiri/tarunai-connect.git#subdirectory=dify-workflow/agent-harness
```

If the upstream project is published to PyPI later, you can replace the first
command with a normal PyPI install.

## Usage

```bash
tarunai-connect-dify-workflow guide
tarunai-connect-dify-workflow list-node-types
tarunai-connect-dify-workflow create -o workflow.yaml --template llm
tarunai-connect-dify-workflow inspect workflow.yaml -j
tarunai-connect-dify-workflow validate workflow.yaml -j
tarunai-connect-dify-workflow edit add-node -f workflow.yaml --type code --title "Process"
```

## Notes

- Most upstream commands support `-j` / `--json-output`.
- The wrapper forwards commands to the installed upstream CLI.
- If `dify-workflow` is not on PATH but the `dify_workflow` Python package is
  installed, the wrapper falls back to `python -m dify_workflow.cli`.

## Run Tests

```bash
python -m pytest tarunai_connect/dify_workflow/tests/ -v
```

## Safety Notes

- This harness only edits local Dify workflow DSL files.
- Review generated YAML/JSON before importing into production Dify projects.
