#!/bin/bash

# start the docker image locally and share the directory one level up


# Notes:

# DPF_DOCKER tells "conftest.py" to resolve all the test files
# relative to the docker image's directory.  Provided that you've
# mapped this source directory over (through -v `pwd`/../:/dpf below).

# DPF_PORT is the port exposed from the DPF container.

# DPF_START_SERVER tells `ansys.dpf.core` not to start an instance and
# rather look for the service running at DPF_IP and DPF_PORT.  If
# those environment variables are undefined, they default to 127.0.0.1
# and 50054 for DPF_IP and DPF_PORT respectively.

source IMAGE_NAME
docker run -it --rm -v `pwd`/../:/dpf -p 50054:50054 --name dpf $IMAGE

