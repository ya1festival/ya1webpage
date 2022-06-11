#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Levin Eric Zimmermann & Roberto Maxwell Beseler"
SITENAME = "ya¹ Tagesfestival für aktuelle Musik"
# SITEURL = 'https://www.ya-festival.org'
SITEURL = "http://127.0.0.1:8000"

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "de"

# Blogroll
LINK_LIST = [
    # ("Link-name", "Link"),
]

# Social widget
SOCIAL = [
    # ("You can add links in your config file", "#"),
    # ("Another social link", "#"),
]

DEFAULT_PAGINATION = 10

THEME = "ya-theme/"

# Title / Link
MENU_ITEM_LIST = [
    [{"de": "1", "en": "1"}, ""],
    [{"de": "performer:innen", "en": "artists"}, "artists"],
    [{"de": "karten", "en": "maps"}, "maps"],
    [{"de": "tickets", "en": "tickets"}, "tickets"],
    [{"de": "team", "en": "team"}, "team"],
]

FOOTER_ITEM_LIST = [
    [{"de": "impressum", "en": "impressum"}, "impressum"],
    [{"de": "datenschutz", "en": "datenschutz"}, "datenschutz"],
    [{"de": "förderer", "en": "sponsors"}, "sponsors"],
]

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
