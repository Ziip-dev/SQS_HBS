"""
Caprover specific settings for deployment.
"""

from .settings import env

# Django environment configuration
DEBUG = env.bool("CR_DEBUG")
SECRET_KEY = env.str("CR_SECRET_KEY")
ALLOWED_HOSTS = env.list("CR_HOSTS")

# Fitapp subscription settings
FITAPP_SUBSCRIBER_ID = env.str("FITAPP_SUBSCRIBER_ID")
FITAPP_VERIFICATION_CODE = env.str("FITAPP_VERIFICATION_CODE")

# HTTP Strict Transport Security
# https://docs.djangoproject.com/en/4.0/ref/middleware/#http-strict-transport-security
# SECURE_HSTS_SECONDS = 2_592_000
SECURE_HSTS_SECONDS = 30
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SSL/HTTPS configuration
# https://docs.djangoproject.com/en/4.0/topics/security/#ssl-https
# Let the proxy manage SSL redirections so to avoid ERR_TOO_MANY_REDIRECTS
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
# Read X-Forwarded-For header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# CSRF settings
# https://docs.djangoproject.com/en/4.0/ref/csrf/#how-csrf-works
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = env.list("CR_TRUSTED_ORIGINS")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
host = env("CR_DB_HOST")
port = env("CR_DB_PORT")
name = env("CR_DB_NAME")
user = env("CR_DB_USER")
password = env("CR_DB_PASSWORD")


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
broker_host = env("CR_BROKER_HOST")
broker_port = env("CR_BROKER_PORT")
broker_user = env("CR_BROKER_USER")
broker_password = env("CR_BROKER_PASSWORD")

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
