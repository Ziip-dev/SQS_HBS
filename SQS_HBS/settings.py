"""
Django settings for SQS_HBS project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env(Path(BASE_DIR, ".env"))

# testing settings
# ANAIS_PASSWORD = env("anais_password")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# Identifiants de l'app perso déclarée sur le compte d'Anaïs
FITAPP_CONSUMER_KEY = env("FITAPP_CONSUMER_KEY")
FITAPP_CONSUMER_SECRET = env("FITAPP_CONSUMER_SECRET")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: this can also be put in .env for production
ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: this is only for test purposes with localtunnel
CSRF_TRUSTED_ORIGINS = ["https://sqshbs-subscription.loca.lt"]


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",  # https://github.com/evansd/whitenoise/blob/master/docs/django.rst#5-using-whitenoise-in-development
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dashboard.apps.DashboardConfig",
    "fitapp",
    "django_simple_bulma",
    "widget_tweaks",
    "silk",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "silk.middleware.SilkyMiddleware",
]

ROOT_URLCONF = "SQS_HBS.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "fitapp.templatetags.fitbit",
            ],
        },
    },
]

WSGI_APPLICATION = "SQS_HBS.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DB_HOST"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "CET"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "static"

STATICFILES_FINDERS = [
    # default ones
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # custom django_simple_bulma one
    "django_simple_bulma.finders.SimpleBulmaFinder",
]

# WhiteNoise configuration for serving static files
# compression + caching
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# compression without caching
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = "home"


# Custom settings for django-simple-bulma
BULMA_SETTINGS = {}


# Celery configuration - uppercase instead of lowercase, and start with CELERY_
CELERY_TIMEZONE = "CET"
# CELERY_BROKER_URL = "amqp://admin:mypass@localhost:5672"
CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
# CELERY_RESULT_BACKEND = "rpc://"
# CELERY_RESULT_BACKEND = "django-db"
CELERY_TASK_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ["json", "pickle"]
# CELERY_WORKER_CONCURRENCY = 1
# os.environ.setdefault('C_FORCE_ROOT', 'true')  # new
# CELERY_ALWAYS_EAGER = True