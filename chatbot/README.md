# Post Singularity Chat Bot
Tags: [meta], [chatbot]

This is a simple Flask web application that answers questions using the markdown
files in this repository. The bot restricts conversation to topics present in
the Post Singularity project and does not invent new lore.

## Usage

```bash
pip install -r requirements.txt
python app.py
```

Open your browser to `http://localhost:5000` and start chatting.

```json
{
  "id": "chatbot_overview",
  "type": "tool",
  "name": "Post Singularity Chat Bot",
  "tags": ["chatbot"],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": ["question answering"]
}
```
