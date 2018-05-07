#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Everton da Rosa <everton3x@gmail.com>'
SITENAME = 'Foguetemodelismo'
SITEURL = 'http://localhost:8000/docs'

PATH = 'content'
OUTPUT_PATH = 'docs'
# PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

STATIC_PATHS = [
    'assets',
    'images',
]

EXTRA_PATH_METADATA = {
    # 'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_DATE_FORMAT = '%d/%m/%Y'
DEFAULT_DATE = 'fs'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

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
# LINKS = (('Everton da Rosa', 'https://everton3x.github.io/'),
# 		# ('Hello World', 'https://everton3x.github.io/helloworld/'),
#         ('Contabilidade Pública', 'https://everton3x.github.io/contabilidadpublica'),
#         ('Fórum sobre Contabilidade Pública', 'http://www.contabeis.com.br/forum/foruns/8/contabilidade-publica/')
# )

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/foguetemodelismo'),
			# ('Twitter', 'https://twitter.com/everton3x'),
          # ('Medium', 'https://medium.com/everton3x'),
          # ('Github', 'https://github.com/everton3x'),
          )

DEFAULT_PAGINATION = 10

# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (('Início', 'index.html'),
	('Foguetemodelismo', 'foguetemodelismo.html'),
	('Water Rockets', 'water-rockets.html'),
	('Projetos', 'projetos.html'),
	('Categorias', 'categories.html'),
	('Tags', 'tags.html'),
	('Autores', 'authors.html'),
	('Arquivos', 'archives.html'),
	('Contribua', 'como-contribuir.html'),
	('Sobre nós', 'sobre.html'),
)
# MENUITEMS = (('Início', SITEURL + '/index.html'),
# 	('Foguetemodelismo', SITEURL + '/pages/foguetemodelismo.html'),
# 	('Water Rockets', SITEURL + '/pages/water-rockets.html'),
# 	('Projetos', SITEURL + '/pages/projetos.html'),
# 	('Categorias', SITEURL + '/categories.html'),
# 	('Tags', SITEURL + '/tags.html'),
# 	('Autores', SITEURL + '/authors.html'),
# 	('Arquivos', SITEURL + '/archives.html'),
# 	('Contribua', SITEURL + '/pages/como-contribuir.html'),
# 	('Sobre nós', SITEURL + '/pages/sobre.html'),
# )

THEME = 'themes/attila'

## Configurações do tema Attila
AUTHORS_BIO = {
    'everton3x': {
        'name': 'Everton da Rosa',
        'website': 'https://everton3x.github.io',
        'location': 'Três de Maio - RS - Brasil',
        'bio': 'Contador por profissão, programador por vocação, e foguetemodelista.',
        'cover': 'https://pt.gravatar.com/userimage/2318180/0a175cf735e882a8c81d12d05952842c.png',
        'image': 'https://pt.gravatar.com/userimage/2318180/0a175cf735e882a8c81d12d05952842c.png',
    }
}

HEADER_COVER = 'assets/images/banner_1.jpg'
# COLOR_SCHEME_CSS = 'tomorrow.css'
# COLOR_SCHEME_CSS = 'tomorrow_night.css'
# COLOR_SCHEME_CSS = 'monokai.css'
COLOR_SCHEME_CSS = 'github.css'
# COLOR_SCHEME_CSS = 'darkly.css'

SHOW_FULL_ARTICLE = False
