import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'source_podliver.settings')

app = Celery('source_podliver')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'get-indigo-profiles': {
        'task': 'indigo.tasks.get_indigo_profiles',
        'schedule': 20.0,
    },
    'get-dolphin-info': {
        'task': 'dolphin.tasks.get_dolphin_info',
        'schedule': 40.0,
    },
    'make-published': {
        'task': 'cfdns.tasks.make_published',
        'schedule': 10.0,
    },
    'clear-db': {
        'task': 'cfdns.tasks.crear_db',
        'schedule': 10.0,
    },
}
