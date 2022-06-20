#!./.venv/bin/python3

"""Script to auto-generate html files."""

import os

import markdown

MARKDOWN_FILES_PATH = "acts/"
HTML_FILES_PATH = "ya-theme/templates/acts"

if __name__ == "__main__":
    for local_markdown_file_path in os.listdir(MARKDOWN_FILES_PATH):
        markdown_file_path = f"{MARKDOWN_FILES_PATH}/{local_markdown_file_path}"
        html_file_path = (
            f"{HTML_FILES_PATH}/{local_markdown_file_path.split('.')[0]}.html"
        )

        with open(markdown_file_path, "r") as markdown_file:
            text = markdown_file.read()
            html = markdown.markdown(text)

        with open(html_file_path, "w") as html_file:
            html_file.write(html)
