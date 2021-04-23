#!/bin/bash
# source /usr/src/app/venv/bin/activate
#source /usr/src/app/venv/bin/postactivate
exec gunicorn  -c "gunicorn.py" hospital.wsgi
