# tasks.py

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .utils import fetch_latest_videos

@shared_task
def fetch_videos_task(api_key, query):
    fetch_latest_videos(api_key, query)
