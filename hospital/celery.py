import os
import subprocess

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')


app = Celery("hospital")


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task
def test():
    print('Celery testing...')


def run_weekly_db_backup():
    subprocess.call("patient/tasks/backup/db_backup.sh")


app.conf.beat_schedule = {
    'add-test-night-weekly': {
        'task': 'tasks.test',
        'schedule': crontab(hour=23, minute=0, day_of_week=6),
        'args': (),
    },
    'add-backup-night-weekly': {
        'task': 'tasks.run_weekly_db_backup',
        'schedule': crontab(hour=0, minute=0, day_of_week=6),
        'args': (),
    },
}