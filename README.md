![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n Docs

This repository hosts the documentation for [n8n](https://n8n.io/), an extendable workflow automation tool which enables you to connect anything to everything. The documentation is live at [docs.n8n.io](https://docs.n8n.io/).

# Datasets
Training datasets for LLM fine-tuning with 3,061+ n8n workflow examples.

* **dataset_001.json** - 3,061 workflow examples (2.5 MB)
* **dataset_002.json** - Additional examples (4.9 MB)
* **dataset_003.json** - Advanced examples (14.0 MB)

See [datasets/README.md](datasets/README.md) for format details and usage.

## Using This Repository for LLM Training

This repository serves two main purposes:
1. **Documentation Website**: Source for [docs.n8n.io](https://docs.n8n.io/) (built with MkDocs)
2. **LLM Training & Reference**: Structured documentation and datasets for AI model training

### 📚 Quick Navigation for LLMs

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

### 🎯 Training Datasets

- **[datasets/README.md](datasets/README.md)** - 3,061+ workflow examples in conversational format
- **dataset_001.json** - 3,061 examples ✅ Valid
- **dataset_002.json** - Additional examples ⚠️ May need repair
- **dataset_003.json** - Advanced examples ⚠️ May need repair

### 🔧 Key n8n Concepts

#### Nodes
Building blocks of workflows. Three main types:
- **Trigger Nodes**: Start workflows (webhooks, schedules, app events)
- **Action Nodes**: Perform operations (send email, create record, API calls)
- **Core Nodes**: Data transformation (Set, Code, If, Switch, Merge)

#### Workflows
Connected sequences of nodes that automate tasks:
```json
{
  "name": "Workflow Name",
  "nodes": [...],
  "connections": {...},
  "active": true/false
}
```

#### Expressions
JavaScript expressions for dynamic data:
- `{{ $json.fieldName }}` - Access current item data
- `{{ $node["Node Name"].json }}` - Reference other node data
- `{{ DateTime.now() }}` - Use utility functions

### ❓ Finding Information

| Question | Location |
|----------|----------|
| Connect to a specific app? | `/docs/integrations/builtin/app-nodes/` |
| Write JavaScript code? | `/docs/code/builtin/code/` |
| Set up webhooks? | `/docs/flow-logic/trigger-nodes/` |
| Deploy n8n? | `/docs/hosting/` |
| Handle errors? | `/docs/flow-logic/error-handling/` |
| Transform data? | `/docs/data/data-transformation/` |
| Use environment variables? | `/docs/hosting/configuration/environment-variables/` |

### 🔍 Common Integrations

Most frequently used (see `/docs/integrations/builtin/app-nodes/`):
- Gmail, Google Sheets, Google Drive, Google Calendar
- Slack, Microsoft Teams, Discord
- Airtable, Notion, Monday
- Stripe, PayPal, Shopify
- GitHub, GitLab, Bitbucket
- OpenAI, Anthropic, Hugging Face

### 🤖 LLM-Optimized Output

Generate `llms-full.txt` - complete documentation in one LLM-friendly file:
```bash
pip install -r requirements.txt
mkdocs build
# Output: llms-full.txt
```

Ideal for: RAG systems, context injection, embeddings, quick reference

### 🔗 Integration with n8n-mcp

**This Repository (n8n-docs)**:
- Static documentation content
- Training datasets for fine-tuning
- Workflow examples and patterns

**n8n-mcp Server**:
- Real-time workflow execution
- Dynamic workflow search
- Integration testing
- Live n8n instance interaction

**Use Together**: Reference this repo for learning n8n, then use n8n-mcp to execute and test workflows.

## Previewing and building the documentation locally

### Prerequisites

* Python 3.8 or above
* Pip
* Follow the [recommended configuration and auto-complete](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration) guidance for the theme. This will help when working with the `mkdocs.yml` file.
* The repo includes a `.editorconfig` file. Make sure your local editor settings **do not override** these settings. In particular:
	- Don't allow your editor to replace tabs with spaces. This can affect our code samples (which must retain tabs for people building nodes).
	- One tab must be equivalent to four spaces.
* n8n recommends using a virtual environment when working with Python, such as [venv](https://docs.python.org/3/tutorial/venv.html).

### Steps

#### For members of the n8n GitHub organization:

n8n members have access to the full Insiders version of the site theme.

1. Set up an SSH token and add it to your GitHub account. Refer to [GitHub | About SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) for guidance.
2. Then run these commands:

	```bash
	git clone --recurse-submodules git@github.com:n8n-io/n8n-docs.git
	cd n8n-docs
 	# Set up a virtual environment (steps depend on your system) and activate it
 	# Install dependencies
	pip install -r requirements.txt
	pip install _submodules/insiders
	```

#### For external contributors:

External contributors don't have access to the full Insiders version of the site theme. You can rely on the preview builds on pull requests, or use the free version of Material for MkDocs.

Fork the repository, then:

```bash
git clone https://github.com/<your-username>/n8n-docs.git
cd n8n-docs
# Set up a virtual environment (steps depend on your system) and activate it
# Install dependencies
pip install -r requirements.txt
pip install mkdocs-material
```

#### To serve a local preview:

```
mkdocs serve --strict
```

## Troubleshooting

### Errors due to missing extensions or features

n8n's docs use the Insiders version of the Material theme. This is not available to external contributors. The standard (free) version has most of the features, but you may get errors if the site is relying on features currently in Insiders. The feature set is constantly changing, as the theme creator gradually moves features out of Insiders to general availability. You can view the currently restricted feautres here: [Material Insiders Benefits](https://squidfunk.github.io/mkdocs-material/insiders/benefits/).

To work around this, you can either:

- Rely on the preview builds when you open a PR.
- Temporarily comment out features in the `mkdocs.yml`. Before committing any changes, remember to uncomment any sections you commented out of the `mkdocs.yml` file.

### Build times

If you find the build times are slow when working with local previews, you can temporarily speed up build times by ignoring parts of the site you're not working on.

#### Dirty builds

`mkdocs serve --strict --dirty`

The first build will still be a full build, but subsequently it will only rebuild files that you change.

#### Temporarily exclude the integrations library

In `mkdocs.yml`, find the `exclude` plugin. Uncomment `- integrations/builtin/*`. Remember to comment it out again before committing.

#### Skip pulling in data for integrations macros

One of the factors that slows down the builds is pulling fresh data for the trending workflows in the integrations pages. You can skip this when previewing locally.

```
# Bash
export NO_TEMPLATE=true && mkdocs serve --strict

# PowerShell
$env:NO_TEMPLATE='true'; mkdocs serve --strict
```

## Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guide.

You can find [style guidance](https://github.com/n8n-io/n8n-docs/wiki/Styles) in the wiki.


## Support

If you have problems or questions, head to n8n's forum: https://community.n8n.io


## License

n8n-docs is [fair-code](https://faircode.io/) licensed under the [**Sustainable Use License**](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).

More information about the license is available in the [License documentation](https://docs.n8n.io/sustainable-use-license).

