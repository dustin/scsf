# Django settings for scsf project.

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

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

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'http://www.santaclaraschoolsfoundation.org/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hajepy*kz13&85(6_2=i8l%t&@)axx^)v&l^7ijm18v6%29a*#'

ROOT_URLCONF = 'scsf.settings.urls.main'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    '/data/web/django/templates/sfsc',
)

INSTALLED_APPS = (
    'scsf.apps.general',
    'scsf.apps.grants',
    'scsf.apps.scholarships',
)
