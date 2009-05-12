# Django settings for scsf project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dustin Sallings', 'dustin@spy.net'),
)

MANAGERS = ADMINS

GRANT_MAIL = ['noelani@spy.net', 'georgelaw@earthlink.net',
    'nbrunyon@yahoo.com', 'keast_43@pacbell.net']

CACHE_BACKEND = 'memcached://purple:11211/'
CACHE_MIDDLEWARE_SECONDS = 30
CACHE_MIDDLEWARE_KEY_PREFIX = 'scsf'

DATABASE_ENGINE = 'postgresql'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'scsf'             # Or path to database file if using sqlite3.
DATABASE_USER = 'scsf2'             # Not used with sqlite3.
DATABASE_PASSWORD = '1qUXpZlixwjx'         # Not used with sqlite3.
DATABASE_HOST = 'purple'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h(yqn70zla3u(p=byl5_y@veb&!amu-27n=va9=7(%0pp1*#wh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'scsf.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    '/data/web/django/templates/scsf/',
)

ALLOWED_INCLUDE_ROOTS = (
    '/data/web/django/templates/scsf/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'scsf.apps.general',
)
