#!/bin/bash
# source /usr/src/app/venv/bin/activate
#source /usr/src/app/venv/bin/postactivate
exec gunicorn  -c "/usr/src/app/gunicorn.py" hospital.wsgi
