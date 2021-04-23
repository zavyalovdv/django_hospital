#!/bin/bash

python3 manage.py makemigrations --no-input

python3 manage.py migrate --no-input

# echo DEBUG = False >> hospital/settings.py

# exec celery --app=hospital worker --loglevel=info &

exec gunicorn hospital.wsgi:application -b 0.0.0.0:8000 --reload
