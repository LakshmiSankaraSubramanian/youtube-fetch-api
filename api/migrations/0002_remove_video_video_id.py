# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-03-26 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_id',
        ),
    ]
