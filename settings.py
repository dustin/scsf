# Django settings for scsf project.

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_GZIP = True
CACHE_MIDDLEWARE_KEY_PREFIX = "scsf"
CACHE_MIDDLEWARE_SECONDS = 300

LANGUAGE_CODE = 'en-us'

DATABASE_ENGINE = 'postgresql' # 'postgresql', 'mysql', or 'sqlite3'.
DATABASE_NAME = 'scsf'             # Or path to database file if using sqlite3.
DATABASE_USER = 'scsf'             # Not used with sqlite3.
DATABASE_PASSWORD = '1qUXpZlixwjx'         # Not used with sqlite3.
DATABASE_HOST = 'db'             # Set to empty string for localhost. Not used with sqlite3.

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    "django.middleware.cache.CacheMiddleware",
    "django.middleware.sessions.SessionMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
)

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'http://www.santaclaraschoolsfoundation.org/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hajepy*kz13&85(6_2=i8l%t&@)axx^)v&l^7ijm18v6%29a*#'

ROOT_URLCONF = 'scsf.urls'

TEMPLATE_LOADERS = (
    'django.core.template.loaders.filesystem.load_template_source',
    'django.core.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    '/data/web/django/templates/scsf/',
)

ALLOWED_INCLUDE_ROOTS = TEMPLATE_DIRS

INSTALLED_APPS = (
    'scsf.apps.general',
    'scsf.apps.grants',
    'scsf.apps.scholarships',
    'scsf.apps.volunteers',
    'scsf.apps.donations',
    'scsf.apps.phoneathon',
    "django.contrib.flatpages",
)
