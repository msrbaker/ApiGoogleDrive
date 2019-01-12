"""
Django settings for gdriveapi project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.utils.text import slugify

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERSION = '0.1.0'
APP_NAME = 'GDrive API'  # Custom fancy name

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('APP_SECRET_KEY',
                       '#mobo0394@*7-_3o@=i+(x^-p&@4acvq-#fw77jq+rsvlq(g2p')

# SECURITY WARNING: don't run with debug turned on in production!
_debug_raw = os.getenv('APP_DEBUG', 'false').lower()
DEBUG = True if _debug_raw == 'true' else False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gdstorage',
    'django_filters',
    'rest_framework',
    'common'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gdriveapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gdriveapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

AUTH_USER_MODEL = 'common.User'

# LOGIN_URL = 'common:login'
# LOGOUT_URL = 'common:logout'
# LOGIN_REDIRECT_URL = 'common:home'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en-us', 'US English'),
    ('es-ar', 'Español de Argentina'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.getenv('APP_FILES_STATIC', os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

MEDIA_ROOT = os.getenv('APP_FILES_MEDIA', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
)

# Google Drive settings
# GDrive auth json file
# https://developers.google.com/identity/protocols/OAuth2ServiceAccount
GDRIVE_CREDS_SERVICE_FILE = os.getenv(
    'APP_GDRIVE_CREDS_SERVICE_FILE',
    os.path.join(BASE_DIR, 'credentials_service.json')
)
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = GDRIVE_CREDS_SERVICE_FILE

# GDrive oauth json file
# https://developers.google.com/drive/api/v3/quickstart/python?refresh=1&pli=1#step_1_turn_on_the
GDRIVE_CREDS_OAUTH_FILE = os.getenv(
    'APP_GDRIVE_CREDS_OAUTH_FILE',
    os.path.join(BASE_DIR, 'credentials_oauth.json')
)

# String to append to the file name in GDrive. It should be a directory name
# but GDrive doesn't create nor uses a dir even if it exists. Anyway, it can
# be i.e. "somedir/" without issue.
GDRIVE_STORAGE_PRENAME = os.getenv('APP_GDRIVE_STORAGE_PRENAME', 'gdrive-api/')

# Email of the user. It's not mandatory, but without it, the file will appear
# as "shared with me" instead of belonging to the user.
GDRIVE_USER_EMAIL = os.getenv('APP_GDRIVE_USER_EMAIL')
# <>

# REST Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions
    # http://www.django-rest-framework.org/api-guide/permissions/
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissions',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': (
        'v1',
    ),
}
# <>

APP_HOST = os.getenv('APP_HOST', 'localhost')   # Host URL/IP
ALLOWED_HOSTS = ['127.0.0.1', APP_HOST]
INTERNAL_IPS = ['127.0.0.1', ]

# Prabandhan Admins
# Comma-separated list of admins names
_admin_names_raw = os.getenv('APP_ADMIN_NAMES', 'root')
# Comma-separated list of admins emails
_admin_emails_raw = os.getenv('APP_ADMIN_EMAILS', 'root@localhost')
_admin_names = [name.strip() for name in _admin_names_raw.split(',')]
_admin_emails = [email.strip() for email in _admin_emails_raw.split(',')]
# List of tuples setting admins emails that will receive error logs
ADMINS = [(name, email) for name, email in zip(_admin_names, _admin_emails)]
# <>

# Email
# APP_EMAIL_SECURITY: Determine security for the email
#   'tls': for ssl/tls
#   'starttls': for starttls
#   'none' or empty: for no SSL at all
_email_encryption = os.getenv('APP_EMAIL_SECURITY', 'none').lower()
EMAIL_USE_TLS = True if _email_encryption == 'tls' else False
EMAIL_USE_SSL = True if _email_encryption == 'startssl' else False
EMAIL_TIMEOUT = 20
EMAIL_USE_LOCALTIME = True
EMAIL_SUBJECT_PREFIX = '[{}] '.format(APP_NAME)
EMAIL_PORT = os.getenv('APP_EMAIL_HOST_PORT')
EMAIL_HOST_USER = os.getenv('APP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('APP_EMAIL_HOST_PASSWORD')
EMAIL_HOST = os.getenv('APP_EMAIL_HOST')
DEFAULT_FROM_EMAIL = os.getenv('APP_EMAIL_FROM',
                               'no-reply@{}.com'.format(slugify(APP_NAME)))
# Set the backend as SMTP only if all parameters are set, else use file
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' \
    if EMAIL_PORT and EMAIL_HOST \
    else 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')
# <>

# Web security
# Determine the way SSL is provided:
#   'proxyssl': if behind an SSL capable proxy
#   'ssl': if it provides SSL by itself w/o proxy
#   'proxy': if it is behind a proxy w/o ssl
#   'none' or empty: for no SSL nor proxy at all
APP_TLS_MODE = os.getenv('APP_TLS_MODE', None)

if APP_TLS_MODE == 'proxyssl':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
if APP_TLS_MODE in ('proxy', 'proxyssl'):
    USE_X_FORWARDED_HOST = True
if APP_TLS_MODE in ('proxyssl', 'ssl'):
    SECURE_SSL_REDIRECT = True
    # Use stepped increments: 86400 604800 2592000 7776000 15768000
    SECURE_HSTS_SECONDS = int(os.getenv('APP_HSTS_SECONDS', 24 * 3600))
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_DOMAIN = APP_HOST
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS
SESSION_COOKIE_DOMAIN = APP_HOST
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = int(os.getenv('APP_SESSION_LIFETIME_SECONDS',
                                   5 * 24 * 3600))
X_FRAME_OPTIONS = 'Deny'
# <>

# Logging
_loglevel_raw = os.getenv('APP_LOG_LEVEL', 'INFO').upper()
_loglevel = _loglevel_raw \
    if _loglevel_raw in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL') \
    else 'INFO'
# Send all to STDERR by default (useful for Docker)
# Send errors by email to ADMINS (which should be defined at local_settings)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} p:{process:d} t:{thread:d} '
                      '[{name}.{funcName}:{lineno:d}] {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
        # 'file': {
        #     'class': 'logging.FileHandler',
        #     'formatter': 'simple',
        #     'filename': os.path.join(BASE_DIR, 'app.log'),
        #     'filters': ['require_debug_true'],
        # },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': _loglevel,
        },
        'rest_framework': {
            'handlers': ['console', 'mail_admins'],
            'level': _loglevel,
        },
        'common': {
            'handlers': ['console', 'mail_admins'],
            'level': _loglevel,
        },
    },
}

# Import local settings and allow current config bypass
try:
    from .local_settings import *
except ImportError:
    pass

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
