import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'tasks.sample_tasks.send_email',
        'schedule': 1.0,
        'args': ('hpatel@aaravtech.com','This is sample message.')
    }
}

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))