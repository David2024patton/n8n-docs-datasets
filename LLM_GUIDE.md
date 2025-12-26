# LLM Guide: n8n Documentation Repository

This guide helps Large Language Models (LLMs) navigate and utilize the n8n documentation and training data effectively.

## Repository Purpose

This repository serves two main purposes:

1. **Documentation Website**: Source for [docs.n8n.io](https://docs.n8n.io/) (built with MkDocs)
2. **LLM Training & Reference**: Structured documentation and datasets for AI model training

## Quick Navigation

### 📚 Core Documentation (`/docs`)

| Topic | Path | Description |
|-------|------|-------------|
| **Integrations** | `/docs/integrations/` | 900+ built-in node integrations |
| **Workflows** | `/docs/workflows/` | Workflow creation, execution, sharing |
| **Code** | `/docs/code/` | JavaScript/Python code nodes, expressions |
| **Hosting** | `/docs/hosting/` | Self-hosting, cloud deployment, configuration |
| **API** | `/docs/api/` | REST API reference |
| **Data Operations** | `/docs/data/` | Data transformation, filtering, merging |
| **Flow Logic** | `/docs/flow-logic/` | Conditional routing, loops, error handling |
| **Credentials** | `/docs/credentials/` | Authentication and secret management |

### 🎯 Training Datasets (`/datasets`)

Contains **3,061+ workflow examples** in conversational format for fine-tuning LLMs to generate n8n workflows.

- **dataset_001.json**: 3,061 examples ✅ Valid
- **dataset_002.json**: Additional examples ⚠️ May need repair
- **dataset_003.json**: Advanced examples ⚠️ May need repair

See `/datasets/README.md` for detailed format specification.

### 🔧 Key n8n Concepts

#### 1. Nodes
Building blocks of workflows. Three main types:
- **Trigger Nodes**: Start workflows (webhooks, schedules, app events)
- **Action Nodes**: Perform operations (send email, create record, API calls)
- **Core Nodes**: Data transformation (Set, Code, If, Switch, Merge)

#### 2. Workflows
Connected sequences of nodes that automate tasks. Structure:
```json
{
  "name": "Workflow Name",
  "nodes": [...],
  "connections": {...},
  "active": true/false
}
```

#### 3. Connections
Define data flow between nodes using:
- **Main Connections**: Primary execution path
- **Multiple Outputs**: Conditional routing (IF node, Switch node)
- **Error Handling**: Separate error paths

#### 4. Expressions
JavaScript expressions for dynamic data:
- `{{ $json.fieldName }}` - Access current item data
- `{{ $node["Node Name"].json }}` - Reference other node data
- `{{ DateTime.now() }}` - Use utility functions

## Finding Specific Information

### ❓ "How do I...?"

| Question | Location |
|----------|----------|
| Connect to a specific app? | `/docs/integrations/builtin/app-nodes/` |
| Write JavaScript code? | `/docs/code/builtin/code/` |
| Set up webhooks? | `/docs/flow-logic/trigger-nodes/` |
| Deploy n8n? | `/docs/hosting/` |
| Handle errors? | `/docs/flow-logic/error-handling/` |
| Transform data? | `/docs/data/data-transformation/` |
| Use environment variables? | `/docs/hosting/configuration/environment-variables/` |

### 🔍 Common Integration Queries

Most frequently used integrations available in `/docs/integrations/builtin/app-nodes/`:
- Gmail, Google Sheets, Google Drive, Google Calendar
- Slack, Microsoft Teams, Discord
- Airtable, Notion, Monday
- Stripe, PayPal, Shopify
- GitHub, GitLab, Bitbucket
- OpenAI, Anthropic, Hugging Face

## Relationship with n8n-mcp

### This Repository (n8n-docs)
- Static documentation content
- Training datasets for fine-tuning
- Workflow examples and patterns
- Conceptual guides

### n8n-mcp Server
- Real-time workflow execution via API
- Dynamic workflow search and retrieval
- Integration testing capabilities
- Live n8n instance interaction

**Use Together**: Reference this repository for learning n8n concepts, then use n8n-mcp to execute and test workflows.

## LLM-Optimized Output

### llms-full.txt
The MkDocs build generates `llms-full.txt` - a complete, LLM-optimized representation of all documentation in a single file.

To generate:
```bash
pip install -r requirements.txt
mkdocs build
# Output: llms-full.txt
```

This file is ideal for:
- RAG (Retrieval-Augmented Generation) systems
- Context injection for LLMs
- Embedding generation
- Quick reference lookup

## Advanced n8n Features

### Sub-workflows
Reusable workflow components referenced by Execute Workflow node.

### Variables
Persistent data storage across workflow executions.

### Webhooks
HTTP endpoints that trigger workflows externally.

### Credentials
Secure storage for API keys, passwords, OAuth tokens.

### Error Workflows
Separate workflows triggered on errors for centralized error handling.

## Best Practices for LLM-Generated Workflows

When generating n8n workflows, ensure:

1. **Valid Node Types**: Use only documented node types from `/docs/integrations/`
2. **Proper Connections**: Maintain execution flow integrity
3. **Expression Syntax**: Use correct `{{ }}` syntax for expressions
4. **Credential References**: Include credential placeholders `{{CREDENTIAL_NAME}}`
5. **Position Coordinates**: Space nodes appropriately (400+ units apart horizontally)

## Example Workflow Structure

```json
{
  "name": "Example Workflow",
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "operation": "send",
        "toEmail": "user@example.com"
      },
      "name": "Send Email",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 1,
      "position": [500, 300]
    }
  ],
  "connections": {
    "Start": {
      "main": [[{
        "node": "Send Email",
        "type": "main",
        "index": 0
      }]]
    }
  },
  "active": false
}
```

## Contributing

When using this repository to train or enhance LLMs:

1. Cite n8n attribution appropriately
2. Respect the [Sustainable Use License](LICENSE.md)
3. Report documentation gaps or errors
4. Share improved models or datasets with the community

## Additional Resources

- **Official Docs**: https://docs.n8n.io/
- **Community Forum**: https://community.n8n.io/
- **GitHub**: https://github.com/n8n-io/n8n
- **Workflow Templates**: https://n8n.io/workflows

---

**Last Updated**: 2025-12-26  
**Repository**: n8n-docs  
**License**: Sustainable Use License
