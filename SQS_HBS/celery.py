from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SQS_HBS.settings")

app = Celery("SQS_HBS")

app.config_from_object("django.conf:settings", namespace="CELERY")

# from django.conf import settings
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)
app.autodiscover_tasks()
