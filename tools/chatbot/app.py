import os
import glob
from flask import Flask, request, render_template_string

app = Flask(__name__)


def load_repo_text():
    texts = {}
    for path in glob.glob('**/*.md', recursive=True):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                texts[path] = f.read().lower()
        except Exception:
            pass
    return texts


repo_texts = load_repo_text()

INDEX_TEMPLATE = """
<!doctype html>
<title>Post Singularity Chat</title>
<h1>Post Singularity Chat Bot</h1>
<form action="/chat" method="post">
  <textarea name="message" rows="4" cols="60"></textarea>
  <br>
  <input type="submit" value="Send"/>
</form>
{% if response %}
  <p><strong>Response:</strong></p>
  <div style="white-space: pre-wrap">{{ response }}</div>
{% endif %}
"""


@app.route('/', methods=['GET'])
def index():
    return render_template_string(INDEX_TEMPLATE)


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form.get('message', '').lower()

    if not is_relevant(message):
        return render_template_string(INDEX_TEMPLATE, response="Please focus on topics related to Post Singularity.")

    response = search_repo(message)
    if not response:
        response = "I don't have information about that in the Post Singularity repository."
    return render_template_string(INDEX_TEMPLATE, response=response)


def is_relevant(msg: str) -> bool:
    keywords = ['post singularity', 'ps', 'singularity']
    for word in keywords:
        if word in msg:
            return True
    for doc in repo_texts.values():
        for token in msg.split():
            if token in doc:
                return True
    return False


def search_repo(query: str) -> str | None:
    terms = query.split()
    for path, text in repo_texts.items():
        for term in terms:
            idx = text.find(term)
            if idx != -1:
                start = max(0, idx - 200)
                end = idx + 200
                snippet = text[start:end].strip()
                return f'From {path}:\n{snippet}'
    return None


if __name__ == '__main__':
    app.run(debug=True)
