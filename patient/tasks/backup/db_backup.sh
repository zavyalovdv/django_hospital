#!/bin/bash

MONTH=`(date +"%m")`
DATE=`(date +"%d-%m-%Y")`

mkdir patient/backups/$MONTH

python3 manage.py dumpdata patient > patient/backups/$MONTH/$DATE-fixtures.json
