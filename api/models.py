# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
    """Model for storing youtube video details"""

    video_id = models.CharField(max_length=200, db_index=True, unique=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnailsUrls = models.URLField()
    channel_id = models.CharField(max_length=500, db_index=True)
    channel_title = models.CharField(max_length=500, blank=True, null=True)
    publishedDateTime = models.DateTimeField(db_index=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ('-publishedDateTime',)
