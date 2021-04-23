#!/bin/bash
source /usr/src/app/venv/bin/activate
#source /usr/src/app/venv/bin/postactivate
exec gunicorn  -c "/usr/src/app/venv/bin/gunicorn/gunicorn.py" hospital.wsgi
