"""

Created by aditya on 23/1/19 at 11:29 PM

"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings')

# load task modules from all registered django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))