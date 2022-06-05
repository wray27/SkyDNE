#!/bin/sh

export FLASK_APP=./netconf_api/index.py

source .venv/bin/activate

flask run -h 0.0.0.0