# Simple static site generator. Requires Python markdown package.
# Converts repo Markdown files to HTML in the "site" directory.
import os
import re
import sys
from pathlib import Path

import markdown

if __package__ in (None, ""):  # direct execution: python tools/generate_site.py
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.markdown_utils import collect_markdown_files, first_json_block, read_text

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


def extract_metadata(md_path):
    """Return metadata dict from a markdown file or None."""
    text = read_text(md_path)
    if text is None:
        return None
    return first_json_block(text)


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


def render_page(text, output_path, title):
    """Render Markdown text into the site template at output_path."""
    html_body = convert_links(markdown.markdown(text, extensions=['extra']))
    prefix = relative_prefix(os.path.relpath(output_path, 'site'))
    content = TEMPLATE.format(prefix=prefix, title=title, body=html_body)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def default_title(md_path):
    return os.path.splitext(os.path.basename(md_path))[0].replace('-', ' ').title()


def convert_file(md_path, output_path):
    render_page(read_text(md_path) or '', output_path, default_title(md_path))


def convert_character_index(md_path, output_path, metadata):
    """Convert characters/index.md inserting generated links."""
    text = read_text(md_path) or ''

    # Replace manual bullet list after the heading
    text = re.sub(r'(###\s*Character Links\n)(?:\s*\n)?(?:\s*-.*\n)+',
                  r'\1' + character_links_md(metadata) + '\n', text)

    render_page(text, output_path, 'Character Index')


def main():
    metadata = {}
    md_files = collect_markdown_files('.')
    for md_path in md_files:
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
