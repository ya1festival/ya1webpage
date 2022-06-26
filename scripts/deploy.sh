#!/usr/bin/bash
./make_content.py
.venv/bin/python3 convert_acts_details.py
.venv/bin/pelican content
cp favicon.ico output/
echo "ya-festival.org" > output/CNAME
.venv/bin/ghp-import output
