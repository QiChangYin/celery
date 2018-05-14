from __future__ import absolute_import
from celery import shared_task
import time

@shared_task(track_started=True)
def plus_1(x, y):
    time.sleep(10)
    return x + y

@shared_task(track_started=True)
def multi_1(x, y):
    time.sleep(30)
    return x * y