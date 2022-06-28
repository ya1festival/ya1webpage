#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Levin Eric Zimmermann & Roberto Maxwell Beseler"
SITENAME = "ya¹ Tagesfestival für aktuelle Musik"
# SITEURL = 'https://ya-festival.org'
SITEURL = "http://127.0.0.1:8000"

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "de"

# Blogroll
LINK_LIST = [
    ("instagram", "https://www.instagram.com/ya1festival/"),
]

# Social widget
SOCIAL = [
    ("instagram", "https://www.instagram.com/ya1festival/"),
]

DEFAULT_PAGINATION = 10

THEME = "ya-theme/"

# Title / Link
# XXX: Footer links are directly defined in 'footer.j2'
MENU_ITEM_LIST = [
    [{"de": "1", "en": "1"}, ""],
    [{"de": "karten", "en": "maps"}, "maps"],
    [{"de": "acts", "en": "acts"}, "acts"],
    [{"de": "tickets", "en": "tickets"}, "tickets"],
    [{"de": "team", "en": "team"}, "team"],
    [{"de": "kontakt", "en": "contact"}, "contact"],
]

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
