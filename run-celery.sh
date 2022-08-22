#!/bin/bash

set -eu

# Activate virtual environment
source /home/ziip/pysetup/.venv/bin/activate

# Run celery worker
celery --app=SQS_HBS worker --loglevel=WARNING --pool=eventlet --concurrency=100

exec "$@"
