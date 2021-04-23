#!/bin/bash
# source /usr/src/app/venv/bin/activate
#source /usr/src/app/venv/bin/postactivate
exec gunicorn  -c "/usr/src/app/django_hospital/gunicorn.py" hospital.wsgi
