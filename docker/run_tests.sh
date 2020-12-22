#!/bin/bash

# Run unit tests from this directory after starting the docker image
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )


export DPF_START_SERVER=False
export DPF_DOCKER=True
export DPF_PORT=50054
pytest $parent_path/.. -vx

