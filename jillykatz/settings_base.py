# Django settings for jillykatz  project.
import os
import socket
import re

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

HOST_NAME = socket.gethostname()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


ADMINS = (
    ('Aaron Merriam', 'aaronmerriam@gmail.com'),
)

# TODO: get this email address.
DEFAULT_FROM_EMAIL = 'jillykatz@example.com'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite_database',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# User-uploaded files
MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')
MEDIA_URL = '/media/'

# Static files
STATIC_ROOT = os.path.join(PROJECT_PATH, '..', "static")
STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'public'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Production installs need to have this environment variable set
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'not-really-a-very-good-secret-key-now-is-it-so-set-a-better-one')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'fusionbox.middleware.GenericTemplateFinderMiddleware',
    # Mezzanine
    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.TemplateForDeviceMiddleware',
    'mezzanine.core.middleware.TemplateForHostMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
    # URLconf include
    'widgy.contrib.urlconf_include.middleware.PatchUrlconfMiddleware',
    # Debug Toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'jillykatz.urls'

AUTH_USER_MODEL = 'accounts.User'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'jillykatz.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',

    # Mezzanine
    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'django.contrib.comments',
    'filebrowser_safe',
    'grappelli_safe',

    # Widgy
    'widgy',
    'widgy.contrib.page_builder',
    'widgy.contrib.form_builder',
    'widgy.contrib.widgy_mezzanine',
    'widgy.contrib.urlconf_include',
    'filer',
    'easy_thumbnails',

    # Toolbox
    'debug_toolbar',
    'fusionbox.core',
    'compressor',
    'fusionbox',
    'south',
    'authtools',
    'betterforms',
    'emailtools',
    'django_extensions',

    # Heroku
    'storages',
    's3_folder_storage',

    # Project Apps
    'jillykatz',
    'accounts',
    'bootstrap',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Mezzanine Settings
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

ADMIN_MENU_ORDER = [
    ('Widgy', (
        'pages.Page',
        'page_builder.Callout',
        'form_builder.Form',
        ('Review queue', 'review_queue.ReviewedVersionCommit'),
    )),
]

# Widgy
WIDGY_MEZZANINE_SITE = 'jillykatz.widgy_site.site'
URLCONF_INCLUDE_CHOICES = []


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    'mezzanine.conf.context_processors.settings',
)

SEND_BROKEN_LINK_EMAILS = True

import imp
WIDGY_ROOT = imp.find_module('widgy')[1]

SCSS_IMPORTS = (
    STATICFILES_DIRS[0] + '/css',
    os.path.join(WIDGY_ROOT, 'static', 'widgy', 'css'),
)

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'python -mscss.tool -C %s' %
     ' '.join(['-I "%s"' % d for d in SCSS_IMPORTS])
     )
)


FORCE_SCRIPT_NAME = ''

# <https://www.owasp.org/index.php/HTTPOnly#Browsers_Supporting_HttpOnly>
SESSION_COOKIE_HTTPONLY = True

# Debug Toolbar Settings
INTERNAL_IPS = (
    '127.0.0.1',
    '63.228.88.83',
    '209.181.77.56',
)

EMAIL_LAYOUT = 'mail/base.html'

IGNORABLE_404_URLS = (
    re.compile(r'\.(php|cgi)$', re.IGNORECASE),
    re.compile(r'^/phpmyadmin/', re.IGNORECASE),
    re.compile(r'^/wp-admin/', re.IGNORECASE),
    re.compile(r'^/cgi-bin/', re.IGNORECASE),
    re.compile(r'^(?!/static/).*\.(css|js)/?$', re.IGNORECASE),
)

try:
    from settings_local import *  # NOQA
except ImportError:
    pass

DATABASE_ENGINE = DATABASES['default']['ENGINE']

# This must go _after_ the cache backends are configured, which could be in
# local settings

if not DEBUG:
    # if not `running in runserver` would be a better condition here
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    )

# at the very bottom of settings
from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())
