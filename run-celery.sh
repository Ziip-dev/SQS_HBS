#!/bin/bash

set -eu

# Activate virtual environment
source /home/ziip/pysetup/.venv/bin/activate

# Update webserver - migrations and staticfiles
python manage.py collectstatic --noinput
python manage.py migrate

# Run celery worker
celery --app=SQS_HBS worker --loglevel=WARNING --pool=eventlet --concurrency=100

exec "$@"
