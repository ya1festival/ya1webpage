#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Levin Eric Zimmermann & Roberto Maxwell Beseler"
SITENAME = "ya¹ Tagesfestival für aktuelle Musik"
SITEURL = "https://ya-festival.org"
# SITEURL = "http://127.0.0.1:8000"

SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = True # To disable this feature
SEO_ENHANCER_OPEN_GRAPH = False  # The default value for this feature
SEO_ENHANCER_TWITTER_CARDS = False  # The default value for this feature

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
    # [{"de": "1", "en": "1"}, ""],
    [{"de": "karte", "en": "map"}, "maps"],
    [{"de": "acts", "en": "acts"}, "acts"],
    [{"de": "tickets", "en": "tickets"}, "tickets"],
    [{"de": "team", "en": "team"}, "team"],
]

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
