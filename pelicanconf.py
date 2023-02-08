AUTHOR = 'Além das Quadras'
SITENAME = 'Além das Quadras'
SITEURL = 'https://alemdasquadras.com.br'
SITEIMAGE = 'alemdasquadras.jpg'
SITEDESCRIPTION = 'Experiências vividas e estudos acadêmicos, onde buscamos uma série de conhecimentos do dia a dia construído nas aulas e nos treinos'

FAVICON = 'favicon.ico'
LOGO = 'logo.jpg'
FIRST_NAME = 'Além das Quadras'
TWITTER_USERNAME = 'alemdasquadras'
ATTRIBUTION = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

TWITTER = 'https://twitter.com/alemdasquadras'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'gzip_cache', 'share_post']

PATH = 'content'
OUTPUT_PATH = 'docs/'
THEME = 'brutalist'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-BR'

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True