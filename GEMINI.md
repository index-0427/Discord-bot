# Gemini Project Notes

## Project: Discord-bot

### Execution Environment
- Python scripts should be run using the virtual environment's executable: `.venv/bin/python3`

### Libraries
- The `openai` library has been migrated to the v1.0.0+ API.
  - **Import:** `from openai import OpenAI`
  - **Initialization:** `client = OpenAI(api_key=...)`
  - **Usage:** `client.chat.completions.create(...)`

### OpenAI Model
- The model used is `gpt-4.1-mini`.
