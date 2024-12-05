"""
Django settings for Cashless project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import sys
from django.core.validators import URLValidator
import os
import logging
logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET')
if len(SECRET_KEY) < 46:
    logger.warning('DJANGO_SECRET must be 50 characters long. run "./manage.py generate_secret_key"')
    # raise ValueError('DJANGO_SECRET must be 50 characters long. run "./manage.py generate_secret_key"')

FERNET_KEY = os.environ.get('FERNET_KEY')
if len(FERNET_KEY) != 44:
    raise ValueError(
        'FERNET_KEY must be 32bit Fernet key :  "from cryptography.fernet import Fernet ; Fernet.generate_key()"')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True' or os.environ.get('DEBUG') == '1'
TEST = os.environ.get('TEST') == 'True' or os.environ.get('TEST') == '1'
DEMO = os.environ.get('DEMO') == 'True' or os.environ.get('DEMO') == '1'

if not DEBUG and os.environ.get('SENTRY_DNS'):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_DNS'),
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.3,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )

ALLOWED_HOSTS = ['*'] if DEBUG else [f'{os.environ.get("DOMAIN")}', ]

# INTERNAL_IPS = ['localhost', '127.0.0.1', '*']
# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'tibiauth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'channels',
    'rest_framework',
    'rest_framework_api_key',
    'APIcashless',
    'webview',
    'administration',
    'epsonprinter',
    'adminsortable2',
    'admin_totals',
    'django_extensions',
    'solo',
    'stdimage',
    'more_admin_filters',
    'fedow_connect',
    'htmxview',
    # 'debug_toolbar',
]


# def show_toolbar_callback(request):
#     return DEBUG
# if DEBUG:
#     DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": 'Cashless.settings.show_toolbar_callback'}
#     INSTALLED_APPS += ['debug_toolbar', ]

# 'channels',
AUTH_USER_MODEL = 'tibiauth.TibiUser'

JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = False
JET_INDEX_DASHBOARD = 'administration.dashboard.CustomIndexDashboard'
JET_DEFAULT_THEME = 'default_custom'

JET_SIDE_MENU_ITEMS = {
    'adminstaff': [
        {'app_label': 'APIcashless', 'label': "Membres & Cartes", 'items': [
            {'name': 'membre'},
            {'name': 'cartecashless'},
            {'name': 'cartemaitresse'},
        ]},
        {'app_label': 'APIcashless', 'label': "Articles", 'items': [
            {'name': 'articles'},
            {'name': 'categorie'},
            {'name': 'groupementcategorie'}
        ]},
        {'app_label': 'APIcashless', 'label': "Points de ventes", 'items': [
            {'name': 'pointdevente'},
            {'name': 'table'},
        ]},
        {'app_label': 'APIcashless', 'label': "Ventes", 'items': [
            {'name': 'articlevendu'},
            {'name': 'commandesauvegarde'},
            {'name': 'cloturecaisse'},
        ]},
        {'app_label': 'APIcashless', 'label': "Configurations", 'items': [
            {'name': 'configuration'},
            {'name': 'appareil'},
        ]},
        {'app_label': 'epsonprinter', 'label': "Imprimantes", 'items': [
            {'name': 'printer'},
        ]},
        {'app_label': 'auth', 'items': [
            {'name': 'tibiauth.tibiuser'},
        ]},
    ],
    'adminmembre': [
        {'app_label': 'APIcashless', 'label': "Membres & Cartes", 'items': [
            {'name': 'membre'},
        ]},
        {'app_label': 'APIcashless', 'label': "Articles", 'items': [
            {'name': 'articles'},
        ]},
    ],
}

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Cashless.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 120

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

WSGI_APPLICATION = 'Cashless.wsgi.application'

# Pour WebSocket :
ASGI_APPLICATION = 'Cashless.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST', 'postgres'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# if 'test' in sys.argv:
#     DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase'
#     }

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework_api_key.permissions.HasAPIKey',
        'rest_framework.permissions.IsAuthenticated',
    ]
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'fr')
TIME_ZONE = os.environ.get('TIME_ZONE', 'Indian/Reunion')

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "www", "media")
MEDIA_URL = '/media/'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', True)

if DEBUG:
    SHELL_PLUS = "ipython"
    # SHELL_PLUS_PRINT_SQL = True
    NOTEBOOK_ARGUMENTS = [
        "--ip",
        "0.0.0.0",
        "--port",
        "8182",
        "--allow-root",
        "--no-browser",
    ]

    IPYTHON_ARGUMENTS = [
        "--ext",
        "django_extensions.management.notebook_extension",
        "--debug",
    ]

    IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

    SHELL_PLUS_POST_IMPORTS = [  # extra things to import in notebook
        ("webview.serializers", ("CarteCashlessSerializer", "PointDeVenteSerializer", "TableSerializerWithCommand")),
        ("administration.ticketZ", ("TicketZ",)),
        ("django.template.loader", ("get_template", "render_to_string")),
        ("datetime", ("datetime", "timedelta")),
        ("json"),
        ("requests"),
        ("fedow_connect.fedow_api", ("FedowAPI",)),
        ("fedow_connect.utils", ("rsa_generator", "sign_message", "verify_signature",
                                 "sign_utf8_string", "get_public_key", "get_private_key",
                                 "hash_hexdigest", "rsa_encrypt_string", "rsa_decrypt_string")),
        (("cryptography.hazmat.primitives"), ("serialization",)),
        #     ("module2.submodule", ("func1", "func2", "class1", "etc"))
        #
    ]
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  # only use in development

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
        'verbose': {
            # 'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            # 'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose' if DEBUG else 'simple',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f"{BASE_DIR}/logs/Djangologfile",
            'formatter': 'simple',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
        },
    },
    'root': {
        'level': 'DEBUG' if DEBUG else 'INFO',
        'handlers': ['console', 'logfile']
    },
}

# Celery Configuration Options
CELERY_TIMEZONE = os.environ.get('TIME_ZONE', 'UTC')
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

BROKER_URL = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://redis:6379/0')

# Déclaration du serveur pour liaison des nouveaux terminaux :
# Check https://github.com/TiBillet/Discovery
url_validator = URLValidator()

LABOUTIK_URL = f"https://{os.environ['DOMAIN']}/"
try:
    url_validator(LABOUTIK_URL)
except Exception as e:
    logger.warning("Error validating LaBoutik url, please check DOMAIN in .env (must be without / . ex : laboutik.tibillet.localhost )")
    raise e


DISCOVERY_URL = os.environ.get('DISCOVERY_URL', 'https://discovery.tibillet.coop/')
try:
    url_validator(DISCOVERY_URL)
except Exception as e:
    logger.error("No DISCOVERY_URL = no device")
    raise e

FEDOW_URL = os.environ.get('FEDOW_URL')
try:
    url_validator(FEDOW_URL)
except Exception as e:
    logger.error("No FEDOW_URL = No blockchain = No Cashless")
    raise e


LESPASS_TENANT_URL = os.environ.get('LESPASS_TENANT_URL')
try:
    url_validator(LESPASS_TENANT_URL)
except Exception as e:
    logger.warning("No LESPASS_TENANT_URL = No Lespass = No refill from stripe, no qrcode scan and no user account")



## Pour les test unitaires plus rapide : ./manage.py test --tag=fast --tag=no-fedow
if 'test' in sys.argv and '--tag=fast' in sys.argv:
    MIGRATION_MODULES = {
        'APIcashless': 'APIcashless.migrations_test',
    }
