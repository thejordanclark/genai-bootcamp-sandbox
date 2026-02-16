# GenAI Bootcamp - Copilot Sandbox

This repository demonstrates safe AI-assisted development in a regulated environment.

## Purpose
- Learn GitHub Copilot capabilities
- Practice audit logging
- Understand IP and compliance implications

## Rules
1. All AI-generated code must be reviewed
2. Label commits with [AI-GENERATED]
3. Log prompts in `logs/ai_usage_log.md`

## Setup
```bash
pip install -r requirements.txt
pytest tests/
```