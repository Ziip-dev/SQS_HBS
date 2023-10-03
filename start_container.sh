#!/bin/bash
app_webserver="SQS_HBS-webserver"
app_celery="SQS_HBS-celery"
tag="0.1.2"

# Build latest webserver image
docker build --file webserver.Dockerfile --pull --rm -t ${app_webserver}:${tag} "."
#
# Build latest celery image
docker build --file celery.Dockerfile    --pull --rm -t ${app_celery}:${tag}    "."

# Run webserver container
docker run --name=${app_webserver} --rm -d -p 80:7000 --env-file=.env ${app_webserver}:${tag}

# Run celery container
docker run --name=${app_celery} --rm -d -p 81:7000 --env-file=.env ${app_celery}:${tag}
