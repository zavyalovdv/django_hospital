#!/bin/bash


source ../venv/bin/activate
pwd
python3 manage.py dumpdata patient > fixtures.json
deactivate
