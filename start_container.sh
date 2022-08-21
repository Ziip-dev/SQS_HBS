#!/bin/bash
app="sqshbs"
tag="0.1.2"

# build latest image version
docker build --file webserver.Dockerfile --pull --rm -t ${app}:${tag} "."

# run container
docker run --name=${app} --rm -d -p 80:7000 \
    --env-file=.env \
    ${app}:${tag}
