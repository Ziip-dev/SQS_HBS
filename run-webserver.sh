#!/bin/bash

set -eu

# Activate virtual environment
source /home/ziip/pysetup/.venv/bin/activate

# Update webserver - migrations and staticfiles
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata questions.json

# Run webserver
gunicorn SQS_HBS.wsgi --bind=0.0.0.0:7000

exec "$@"
