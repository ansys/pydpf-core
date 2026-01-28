#!/usr/bin/env bash

if [ -z "$AWP_ROOT222" ]
then
      awp_root=${awp_root:-}
else
      awp_root=${awp_root:-${AWP_ROOT222}}
fi

pip_args=${pip_args:- }

while [ $# -gt 0 ]; do

   if [[ $1 == *"-"* ]]; then
        param="${1/-/}"
        declare $param="$2"
        # echo $1 $2 // Optional to see the parameter:value result
   fi

  shift
done

PYTHON=${awp_root}/commonfiles/CPython/3_7/linx64/Release/python/runpython

export LD_LIBRARY_PATH=${awp_root}/commonfiles/CPython/3_7/linx64/Release/python/lib:{LD_LIBRARY_PATH}

if [ -z "$pip_args" ]
then
/bin/bash: :wq: command not found
else
  ${PYTHON} -m pip install ansys-dpf-core $pip_args
fi
