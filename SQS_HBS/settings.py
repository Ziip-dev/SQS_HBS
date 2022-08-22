"""
Environment agnostic Django settings for SQS_HBS project.
"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Initialise environment variables - use .env file if we are not on Caprover
# env = environ.Env(DEBUG=(bool, False), ALLOWED_HOSTS=(list, []))
# environ.Env.read_env(Path(BASE_DIR, ".env"))
env = environ.Env()
if env("CAPROVER") is None:
    env.read_env(Path(BASE_DIR, ".env"))


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # use whitenoise even in development https://github.com/evansd/whitenoise/blob/main/docs/django.rst#5-using-whitenoise-in-development
    "whitenoise.runserver_nostatic",
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
        "DIRS": [Path(BASE_DIR, "SQS_HBS", "templates")],
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

STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = "static/"

STATICFILES_DIRS = [Path(BASE_DIR, "SQS_HBS", "static")]

STATICFILES_FINDERS = [
    # default ones
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # custom django_simple_bulma one
    "django_simple_bulma.finders.SimpleBulmaFinder",
]

# WhiteNoise configuration for serving static files (compression + cache)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = "home"


# Enable SILK authentication
SILKY_AUTHENTICATION = True
SILKY_AUTHORISATION = True
SILKY_META = True


# Custom settings for django-simple-bulma
# =======================================
BULMA_SETTINGS = {
    # "extensions": [
    #     "bulma-pageloader",
    # ],
    "variables": {
        # Theme color scheme
        "background": "#f6fafc",
        "box-background": "#d8edd9",
        "text-1": "#a956a5",
        "blue-alt-1": "#9594b7",
        "blue-alt-2": "#7fb1df",
        "blue-alt-3": "#a6d1de",
        "text-2": "$blue-alt-1",
        # // Update Bulma's global variables
        # $family-sans-serif: "Nunito", sans-serif;
        "primary": "$text-1",
        "grey-light": "$text-2",
        "widescreen-enabled": "false",
        "fullhd-enabled": "false",
        # Update some of Bulma's component variables
        "body-background-color": "$background",
        "box-background-color": "$box-background",
        "box-color": "$text-1",
        "radius-large": "30px",
        # $control-border-width: 2px;
        # $input-border-color: transparent;
        # $input-shadow: none;
    },
    "output_style": "compressed",
}


# Keys to access Fitbit server app
# ================================
FITAPP_CONSUMER_KEY = env("FITAPP_CONSUMER_KEY")
FITAPP_CONSUMER_SECRET = env("FITAPP_CONSUMER_SECRET")


# ENVIRONMENT RELATED SETTINGS
# ============================

if env("CAPROVER") is None:
    # trunk-ignore(flake8/F401)
    # trunk-ignore(flake8/F403)
    from .settings_dev import *

    # from .settings_dev import (SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DATABASES, CELERY_TIMEZONE, CELERY_BROKER_URL, CELERY_TASK_SERIALIZER, CELERY_ACCEPT_CONTENT)
else:
    # trunk-ignore(flake8/F401)
    # trunk-ignore(flake8/F403)
    from .settings_caprover import *

    # from .settings_caprover import (DEBUG, SECRET_KEY, SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE, SECURE_HSTS_PRELOAD, ALLOWED_HOSTS, DATABASES, CELERY_BROKER_URL, CELERY_TASK_SERIALIZER, CELERY_ACCEPT_CONTENT, CELERY_TIMEZONE)
