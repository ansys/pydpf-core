#!/usr/bin/env bash


pluginpath=${pluginpath:- }
zippath=${zippath:- }
pythonexe=${pythonexe:-python}
tempfolder=${tempfolder:-/tmp}


while [ $# -gt 0 ]; do

   if [[ $1 == *"-"* ]]; then
        param="${1/-/}"
        declare $param="$2"
        # echo $1 $2 // Optional to see the parameter:value result
   fi

  shift
done


echo "Running script with args:"
echo "-pluginpath" ${pluginpath}
echo "-zippath" ${zippath}
echo "-pythonexe" ${pythonexe}
echo "-tempfolder" ${tempfolder}


echo "make venv"
if [ -d "${tempfolder}/venv" ]; then rm -Rf ${tempfolder}/venv; fi

export PYTHONLIBPATH="$(dirname "${pythonexe}")"
echo "adding python so to LD_LIBRARY_PATH"
export LD_LIBRARY_PATH=${PYTHONLIBPATH}/../lib:{LD_LIBRARY_PATH}

${pythonexe} -m venv ${tempfolder}/venv

echo "activate venv"
source ${tempfolder}/venv/bin/activate

echo "install deps"
python -m pip install -r ${pluginpath}/requirements.txt --disable-pip-version-check --use-pep517

SITES=$(find ${tempfolder}/venv/ -type d -name "site-packages")
echo "SITES"
echo ${SITES}

if [ -d "${SITES}/__pycache__" ]; then rm -Rf ${SITES}/__pycache__; fi
DIR="$(dirname "${zippath}")"
if [ ! -d "${DIR}" ]; then mkdir ${DIR}; fi
cd ${SITES}
ls .
python -m zipfile -c ${zippath} *

rm -r ${tempfolder}/venv