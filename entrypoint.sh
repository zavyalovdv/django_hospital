#!/bin/bash

python3 manage.py makemigrations --no-input

python3 manage.py migrate --no-input

exec gunicorn hospital.wsgi:application -b 0.0.0.0:8000 --reload