"""
    ### Look into the below mentioned uris for configuring celery with django
        - https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html?highlight=django#using-celery-with-django
        - https://github.com/celery/django-celery-beat
    ### Celery Config

"""


import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mr_vod.settings')

# django project we are going to use for running selenium test cases.
app = Celery('mr_vod')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

"""Celery Beat Settings"""

# Load task modules from all registered Django apps.
# This function will look into tasks.py in all the apps inside the project
app.autodiscover_tasks()
