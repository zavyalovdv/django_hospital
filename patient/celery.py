import os

from celery import Celery
from celery.schedules import crontab
 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patient.settings')
 
app = Celery('patient')
app.config_from_object('django.conf:settings')
 
app.autodiscover_tasks()
 
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'patient.tasks.backup.run',
        'schedule': crontab(),
    },
}
