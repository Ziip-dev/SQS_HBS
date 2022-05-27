#!/bin/bash

set -eu

# Activate virtual environment
source /home/ziip/pysetup/.venv/bin/activate

# Setup server
# migrations if needed
python manage.py collectstatic --noinput

# Evaluating passed command:
# gunicorn -b :5001 wsgi --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
python manage.py runserver 0.0.0.0:7000

exec "$@"
