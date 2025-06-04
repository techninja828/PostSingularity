# Simple static site generator. Requires Python markdown package.
# Converts repo Markdown files to HTML in the "site" directory.
import os
import json
import markdown
import re

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <link rel='stylesheet' href='{prefix}styles.css'>
  <title>{title}</title>
</head>
<body>
<nav><a href='{prefix}index.html'>Home</a></nav>
{body}
</body>
</html>
"""

LINK_RE = re.compile(r'href="([^"]+\.md)"')

JSON_RE = re.compile(r'```json\s*(\{.*?\})\s*```', re.DOTALL)


def extract_metadata(md_path):
    """Return metadata dict from a markdown file or None."""
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    m = JSON_RE.search(text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def character_links_md(metadata):
    """Return markdown bullet list for characters sorted by name."""
    entries = []
    for path, meta in metadata.items():
        rel = os.path.relpath(path, '.')
        if rel.startswith(os.path.join('characters', '')) and not rel.endswith('index.md'):
            name = meta.get('name')
            if name:
                md_path = os.path.join('characters', os.path.basename(rel))
                entries.append((name, md_path))
    entries.sort(key=lambda x: x[0])
    return '\n'.join(f'- [{name}]({path})' for name, path in entries)


def convert_links(html):
    return LINK_RE.sub(lambda m: f'href="{m.group(1)[:-3]}.html"', html)


def relative_prefix(relpath):
    parts = relpath.split(os.sep)[:-1]
    return '../' * len(parts)


def convert_file(md_path, output_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    html_body = markdown.markdown(text, extensions=['extra'])
    html_body = convert_links(html_body)

    rel = os.path.relpath(output_path, 'site')
    prefix = relative_prefix(rel)

    title = os.path.splitext(os.path.basename(md_path))[0].replace('-', ' ').title()
    content = TEMPLATE.format(prefix=prefix, title=title, body=html_body)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def convert_character_index(md_path, output_path, metadata):
    """Convert characters/index.md inserting generated links."""
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace manual bullet list after the heading
    text = re.sub(r'(###\s*Character Links\n)(?:\s*\n)?(?:\s*-.*\n)+',
                  r'\1' + character_links_md(metadata) + '\n', text)

    html_body = markdown.markdown(text, extensions=['extra'])
    html_body = convert_links(html_body)

    rel = os.path.relpath(output_path, 'site')
    prefix = relative_prefix(rel)
    title = 'Character Index'
    content = TEMPLATE.format(prefix=prefix, title=title, body=html_body)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    metadata = {}
    md_files = []
    for root, _, files in os.walk('.'):  # scan repo
        for name in files:
            if name.endswith('.md'):
                md_path = os.path.join(root, name)
                md_files.append(md_path)
                meta = extract_metadata(md_path)
                if meta:
                    metadata[md_path] = meta

    for md_path in md_files:
        rel_path = os.path.relpath(md_path, '.')
        out_path = os.path.join('site', rel_path[:-3] + '.html')
        if rel_path == os.path.join('characters', 'index.md'):
            convert_character_index(md_path, out_path, metadata)
        else:
            convert_file(md_path, out_path)

    # copy stylesheet
    css_path = os.path.join('site', 'styles.css')
    if not os.path.exists('site'):
        os.makedirs('site')
    if not os.path.exists(css_path):
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(DEFAULT_CSS)


DEFAULT_CSS = """
body { font-family: Arial, sans-serif; margin: 2rem; }
nav { margin-bottom: 1rem; }
nav a { margin-right: 1rem; }
pre, code { background-color: #f4f4f4; padding: 0.2rem 0.4rem; }
"""

if __name__ == '__main__':
    main()
