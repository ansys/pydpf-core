#!/bin/bash

source IMAGE_NAME
docker build -t $IMAGE .
# docker push $IMAGE
