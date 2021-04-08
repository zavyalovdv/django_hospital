command = '/usr/src/app/venv/bin/gunicorn'
pythonpath = '/usr/src/app/django_hospital/hospital'
bind = '127.0.0.1:8000'
workers = 1
user = 'ubuntu'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=hospital.settings'
