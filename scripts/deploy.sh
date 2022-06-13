#!/usr/bin/bash
./make_content.py
.venv/bin/pelican content
echo "https://www.ya-festival.org" > output/CNAME
.venv/bin/ghp-import output
