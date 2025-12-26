# n8n Workflow Training Datasets

This directory contains training datasets for fine-tuning Large Language Models (LLMs) to generate n8n workflows from natural language descriptions.

## Dataset Format

Each dataset file is a JSON array containing training examples in a conversational format:

```json
[
  {
    "messages": [
      {
        "role": "user",
        "content": "When a new email arrives in Gmail, save the attachment to Google Drive."
      },
      {
        "role": "assistant",
        "content": "{\"name\": \"Email to Drive\", \"nodes\": [...], \"connections\": {...}, \"active\": false}"
      }
    ]
  }
]
```

### Structure

- **`role: "user"`** - Natural language description of the workflow to create
- **`role: "assistant"`** - JSON representation of the complete n8n workflow

The assistant's response contains a valid n8n workflow definition with:
- `name`: Workflow name
- `nodes`: Array of node definitions (triggers, actions, transformations)
- `connections`: Object defining how nodes are connected
- `active`: Boolean indicating if workflow is active (usually `false` for templates)

## Dataset Files

### dataset_001.json
- **Size**: 2.5 MB
- **Examples**: 3,061 workflow examples
- **Status**: ✅ Valid JSON
- **Focus**: Common workflow patterns (Gmail, Slack, Google Sheets, Trello, Airtable, Notion, etc.)

### dataset_002.json
- **Size**: 4.9 MB
- **Status**: ⚠️ JSON parsing errors detected
- **Note**: May require cleaning before use

### dataset_003.json
- **Size**: 14.0 MB
- **Status**: ⚠️ JSON parsing errors detected
- **Note**: May require cleaning before use

## Common Workflow Patterns

Based on dataset_001.json analysis, the most common patterns include:

1. **Email Automation**
   - Gmail → Google Drive (save attachments)
   - Gmail → Slack (notifications)
   - Gmail → Airtable (create records)

2. **Spreadsheet Integration**
   - Google Sheets → Slack (new row notifications)
   - Google Sheets → Gmail (alerts)
   - Airtable → Google Sheets (sync data)

3. **Project Management**
   - Trello → Slack (card updates)
   - Trello → Google Calendar (deadline tracking)
   - GitHub → Trello (issue tracking)

4. **Notification Workflows**
   - Slack reactions → Airtable (logging)
   - Calendar events → Email reminders
   - Notion updates → Slack posts

## Usage for LLM Training

### Fine-tuning Format

These datasets are compatible with OpenAI's fine-tuning format and similar training pipelines. Each example teaches the model to:

1. Parse natural language workflow requests
2. Identify required n8n nodes
3. Configure node parameters
4. Establish proper connections between nodes

### Recommended Preprocessing

Before using these datasets:

1. **Validate JSON**: Verify all files parse correctly
2. **Deduplicate**: Remove duplicate examples (some duplicates exist)
3. **Filter**: Optionally filter by specific integrations or complexity
4. **Balance**: Ensure diverse node types are represented

### Example Use Cases

- Fine-tune GPT models to generate n8n workflows
- Train models to suggest workflow improvements
- Create workflow completion assistants
- Build n8n-specific code generation tools

## Integration with n8n-mcp

This repository complements the [n8n-mcp](https://github.com/yourusername/n8n-mcp) server by providing:

- **Static training data** for model fine-tuning
- **Example workflows** for reference
- **Pattern library** for common automations

While n8n-mcp provides real-time workflow execution and API access, these datasets enable LLMs to learn n8n's workflow generation patterns.

## Contributing

When adding new examples:

1. Follow the existing JSON structure
2. Ensure workflow JSON is valid n8n format
3. Use descriptive, natural language in user messages
4. Test workflows before adding to datasets
5. Avoid duplicates

## Known Issues

- Duplicate entries exist in dataset_001.json (minimal impact on training)
- dataset_002.json and dataset_003.json have JSON formatting errors
- Some placeholder values (e.g., `{{SHEET_ID}}`, `{{API_KEY}}`) are included - these are intentional for template-style workflows

## Tools

See `/scripts/analyze_datasets.py` for dataset analysis and statistics tools.
