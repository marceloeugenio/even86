import os
from pathlib import Path

from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")
GOOGLE_RECAPTCHA_SECRET_KEY = config("GOOGLE_RECAPTCHA_SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["even86.herokuapp.com", "localhost", "*"]
DOMAIN = "http://www.even86.com.br"

ADMINS = (("Marcelo Eugenio", "marcelo.eugenio@gmail.com"),)

DATE_FORMAT = "d-m-Y"
DATE_INPUT_FORMATS = ["%d-%m-%Y"]
USE_L10N = False

AUTH_USER_MODEL = "usuario.Usuario"

INSTALLED_APPS = [
    # My apps
    "apps.home",
    "apps.usuario",
    "apps.evento",
    "apps.eventoCategoria",
    "apps.eventoFormato",
    "apps.eventoTipo",
    "apps.inscricao",
    "apps.acessoRecepcao",
    "apps.ajuda",
    "apps.atividade",
    "apps.credenciamento",
    "apps.feedback",
    "apps.geradorCertificados",
    "apps.geradorCracha",
    "apps.importarExportar",
    "apps.pessoas",
    "apps.programacao",
    "apps.submissoes",
    "apps.submissoesControle",
    "apps.transmissaoOnline",
    "apps.validacaoCertificado",
    "apps.organizadores",

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Libs
    'rest_framework',
    'matplotlib',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'even86.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'even86.wsgi.application'

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
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


LANGUAGE_CODE = "pt-br"
USE_I18N = True
TIME_ZONE = "America/Fortaleza"
USE_TZ = True
# USE_L10N = True

MEDIA_URL = "/media/"
MEDIA_ROOT = "media"

LOGIN_URL = "/login/"
# LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_REDIRECT_URL = "conta_alterar"
AUTH_USER_MODEL = "usuario.Usuario"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = ["files_static"]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SERVER_EMAIL = config("SERVER_EMAIL")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
