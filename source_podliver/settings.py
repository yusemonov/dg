from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ')y0fs*b+pkef6^mn$2v2w2i)b97c-j+i(do7)n+6f^+%t80r!+'

DEBUG = True

ALLOWED_HOSTS = ['po.a13.team', '168.119.185.104']


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'indigo',
    'import_export',
    'farming',
    'fbprofiles',
    'cfdns',
    'dolphin',
    'idgenerator',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'source_podliver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'source_podliver.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_po',
        'USER': 'podliver',
        'PASSWORD': 'Mail123123',
        'HOST': 'localhost',
        'PORT': '',
    }
}


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
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 103400  # higher than the count of fields

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

''' MY SETTINGS '''
''' FILE BROWSER'''
# FILEBROWSER_MEDIA_URL = STATIC_ROOT


''' FILE BROWSER'''
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.'
                   'FileBasedCache',
        'LOCATION': '/var/cache/source_podliver/cache',
    }
}


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
''' CELERY SETTINGS '''
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'


''' CELERY SETTINGS '''

''' MODELS SETTINGS '''

JAZZMIN_SETTINGS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user":
                                    "collapsible",
                                    "auth.group":
                                    "vertical_tabs"},


    "custom_links": {
        "idgenerator": [{
            # Any Name you like
            "name": "Генератор паспорта",

            # url name e.g `admin:index`, relative urls e.g `/admin/index` or absolute urls e.g `https://domain.com/admin/index`
            "url": "https://po.a13.team/idgen",

            # any font-awesome icon, see list here https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2 (optional)
            "icon": "fas fa-comments",

            # a list of permissions the user must have to see this link (optional)
            # "permissions": ["books.view_book"]
        }]
    },
}
# JAZZMIN_SETTINGS["show_ui_builder"] = True


INTERNAL_IPS = [
    '93.73.62.199'
]
