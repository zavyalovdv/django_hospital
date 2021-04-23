#!/bin/bash
# source /usr/src/app/venv/bin/activate
#source /usr/src/app/venv/bin/postactivate
exec gunicorn  -c "~/.local/lib/python3.8/site-packages/gunicorn.py" /usr/src/app/django_hospital/hospital/hospital.wsgi
