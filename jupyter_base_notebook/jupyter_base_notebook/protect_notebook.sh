#!/usr/bin/env bash

ep=`python -c 'from notebook.auth import passwd; from os import getenv; hash = passwd(getenv("JUPYTER_PASSWORD")); print(hash)'`

cat ./jupyter_notebook_config.py.tmp| sed 's/ECRYPTED_PASSWORD/'"$ep"'/g' > /home/jovyan/.jupyter/jupyter_notebook_config.py

