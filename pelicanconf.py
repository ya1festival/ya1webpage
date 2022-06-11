#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Levin Eric Zimmermann & Roberto Maxwell Beseler"
SITENAME = "ya¹ Tagesfestival für aktuelle Musik"
# SITEURL = 'https://www.ya-festival.org'
SITEURL = ""

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
    ["1", "/"],
    [{"de": "performer:innen", "en": "artists"}, "artists"],
    [{"de": "karten", "en": "maps"}, "maps"],
    [{"de": "tickets", "en": "tickets"}, "tickets"],
    [{"de": "team", "en": "team"}, "team"],
    # ["impressum", "impressum"],
    # ["datenschutz", "datenschutz"],
    # ["förderer", "sponsors"],
]

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
