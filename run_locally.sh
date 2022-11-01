#!/bin/bash
eval $(ssh-agent)
ssh-add
DOCKER_BUILDKIT=1 docker build --ssh default -t celery-example:dev .
docker run --network="host" --rm --ulimit core=0 --gpus=all --ipc=host --env-file dev.env -v ~/.cache:/root/.cache/ celery-example:dev
