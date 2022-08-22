"""
Local development server settings for SQS_HBS project.
"""

from .settings import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "SECRET_KEY", default="thisisadevelopmentlocalkey,getabetterlookingoneforproduction"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: this can also be put in .env for production
ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: this is only for test purposes with localtunnel
CSRF_TRUSTED_ORIGINS = ["https://sqshbs-subscription.loca.lt"]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "NAME": "dev-db",
        "USER": "ziip",
        "PASSWORD": "supersecretdevpassword",
    }
}


# Celery configuration - uppercase instead of lowercase, and start with CELERY_
# =============================================================================
CELERY_TIMEZONE = "CET"
CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_TASK_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ["json", "pickle"]
