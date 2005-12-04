# Django settings for scsf project.

from scsf.settings import *

ADMIN_FOR = ('scsf.settings')

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

SITE_ID = 2

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    "django.middleware.sessions.SessionMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
)

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'http://admin.santaclaraschoolsfoundation.org/media/'

ROOT_URLCONF = 'scsf.adminurls'

TEMPLATE_LOADERS = (
    'django.core.template.loaders.filesystem.load_template_source',
    'django.core.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    '/data/web/django/templates/scsf-admin/',
)

ALLOWED_INCLUDE_ROOTS = TEMPLATE_DIRS

INSTALLED_APPS = (
    'scsf.apps.general',
    'scsf.apps.grants',
    'scsf.apps.scholarships',
    'scsf.apps.volunteers',
    'scsf.apps.donations',
    'scsf.apps.phoneathon',
    'django.contrib.admin',
    "django.contrib.flatpages",
)
