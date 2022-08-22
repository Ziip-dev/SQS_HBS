"""
Caprover specific settings for deployment.
"""

from django.core.exceptions import ImproperlyConfigured

from .settings import env

# Django environment configuration
DEBUG = False
SECRET_KEY = env("CR_SECRET_KEY") or ImproperlyConfigured("CR_SECRET_KEY not set")

# HTTP Strict Transport Security
# https://docs.djangoproject.com/en/4.0/ref/middleware/#http-strict-transport-security
SECURE_HSTS_SECONDS = 30
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SSL/HTTPS configuration
# https://docs.djangoproject.com/en/4.0/topics/security/#ssl-https
# Let the proxy manage SSL redirections so to avoid ERR_TOO_MANY_REDIRECTS
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True

# Allowed hosts get parsed from a comma-separated list
hosts = env("CR_HOSTS") or ImproperlyConfigured("CR_HOSTS not set")
try:
    ALLOWED_HOSTS = hosts.split(",")
# trunk-ignore(flake8/E722)
except:
    raise ImproperlyConfigured("CR_HOSTS could not be parsed")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
host = env("CR_DB_HOST") or ImproperlyConfigured("CR_DB_HOST not set")
port = env("CR_DB_PORT") or ImproperlyConfigured("CR_DB_PORT not set")
name = env("CR_DB_NAME") or ImproperlyConfigured("CR_DB_NAME not set")
user = env("CR_DB_USER") or ImproperlyConfigured("CR_DB_USER not set")
password = env("CR_DB_PASSWORD") or ImproperlyConfigured("CR_DB_PASSWORD not set")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": host,
        "PORT": port,
        "NAME": name,
        "USER": user,
        "PASSWORD": password,
    }
}


# Celery configuration - uppercase instead of lowercase, and start with CELERY_
# =============================================================================
broker_host = env("CR_BROKER_HOST") or ImproperlyConfigured("CR_BROKER_HOST not set")
broker_port = env("CR_BROKER_PORT") or ImproperlyConfigured("CR_BROKER_PORT not set")
broker_user = env("CR_BROKER_USER") or ImproperlyConfigured("CR_BROKER_USER not set")
broker_password = env("CR_BROKER_PASSWORD") or ImproperlyConfigured(
    "CR_BROKER_PASSWORD not set"
)

CELERY_BROKER_URL = (
    f"amqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}"
)
CELERY_TASK_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ["json", "pickle"]
CELERY_TIMEZONE = "CET"
# https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html#django-celery-results-using-the-django-orm-cache-as-a-result-backend
# CELERY_RESULT_BACKEND = "rpc://"
# CELERY_RESULT_BACKEND = "django-db"

# CELERY_ALWAYS_EAGER = True
