#!/bin/bash

set -eu

# Activate virtual environment
source /home/ziip/pysetup/.venv/bin/activate

# Update webserver - migrations and staticfiles
python manage.py collectstatic --noinput
python manage.py migrate

# EITHER run webserver
gunicorn SQS_HBS.wsgi --bind=0.0.0.0:7000

# OR celery worker
# celery --app=SQS_HBS worker --loglevel=INFO --pool=eventlet --concurrency=100

exec "$@"
