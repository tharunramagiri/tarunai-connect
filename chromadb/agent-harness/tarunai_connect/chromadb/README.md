# tarunAI Connect ChromaDB

CLI harness for ChromaDB vector database using the tarunai-connect methodology.

## Installation

```bash
cd agent-harness
pip install -e .
```

## Usage

### Interactive REPL (default)
```bash
tarunai-connect-chromadb
```

### Direct commands
```bash
# Server
tarunai-connect-chromadb server heartbeat
tarunai-connect-chromadb server version

# Collections
tarunai-connect-chromadb collection list
tarunai-connect-chromadb collection info hub_knowledge
tarunai-connect-chromadb collection create --name test_collection
tarunai-connect-chromadb collection delete --name test_collection

# Documents
tarunai-connect-chromadb document count --collection hub_knowledge
tarunai-connect-chromadb document get --collection hub_knowledge --limit 5
tarunai-connect-chromadb document add --collection hub_knowledge --id doc1 --document "Hello world"
tarunai-connect-chromadb document delete --collection hub_knowledge --id doc1

# Semantic search
tarunai-connect-chromadb query search --collection hub_knowledge --text "how does the pipeline work" --n-results 3
```

### JSON output
Add `--json` before any subcommand:
```bash
tarunai-connect-chromadb --json collection list
tarunai-connect-chromadb --json query search --collection hub_knowledge --text "pipeline" --n-results 3
```

## Configuration

- Default server: `http://localhost:8000`
- Override with `--host`: `tarunai-connect-chromadb --host http://other:8000 server heartbeat`
- Tenant: `default_tenant`, Database: `default_database`
