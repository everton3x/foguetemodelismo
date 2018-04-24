#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Everton da Rosa <everton3x@gmail.com>'
SITENAME = 'Foguetemodelismo'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [
    'assets',
    'images',
]

EXTRA_PATH_METADATA = {
    # 'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
}

# Coloca a landing-page como index
#TEMPLATE_PAGES = {'extra/index.html': 'index.html'}
# Coloca o index origianl com outro nome de página
# INDEX_SAVE_AS = 'blog.html'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/attila'

## Configurações do tema Attila
AUTHORS_BIO = {
    'everton3x': {
        'name': 'Everton da Rosa',
        'website': 'https://everton3x.github.io',
        'location': 'Três de Maio - RS - Brasil',
        'bio': 'Contador por profissão, programador por vocação, e foguetemodelista.'
    }
}

HEADER_COVER = 'assets/images/banner_1.jpg'
# COLOR_SCHEME_CSS = 'tomorrow.css'
# COLOR_SCHEME_CSS = 'tomorrow_night.css'
# COLOR_SCHEME_CSS = 'monokai.css'
COLOR_SCHEME_CSS = 'github.css'
# COLOR_SCHEME_CSS = 'darkly.css'

SHOW_FULL_ARTICLE = False
