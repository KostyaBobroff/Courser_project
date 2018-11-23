from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_house.settings')

app = Celery('smart_house')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

from house.tasks import api
# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'he',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'

# @app.task
# def he():
#     print('api()')

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(5, api.s(), name='Check Smart Home')
#     # app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     # 'read-api-every-5-seconds': {
#     #     'task': 'he',
#     #     'schedule': crontab(second=5)
#     #
#     # },
# # }

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'house.tasks.api',
        'schedule': 5.0

    },
}
app.conf.timezone = 'UTC'