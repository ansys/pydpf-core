#!/bin/bash

# start the docker image locally and share the directory one level up

source IMAGE_NAME
docker run -it --rm -v `pwd`/../:/dpf -p 50054:50054 --name dpf $IMAGE

# On CI:
# docker run -v `pwd`:/dpf -p $DPF_PORT:50054 --name dpf $IMAGE
