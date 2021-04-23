#!/bin/bash

MONTH=`(date +"%m")`
DATE=`(date +"%d-%m-%Y")`

source ../venv/bin/activate

mkdir patient/backups/$MONTH
git add patient/backups/$MONTH

python3 manage.py dumpdata patient > patient/backups/$MONTH/$DATE-fixtures.json

deactivate
