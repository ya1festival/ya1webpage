#!/usr/bin/bash
./make_content.py
.venv/bin/pelican content
.venv/bin/ghp-import output
