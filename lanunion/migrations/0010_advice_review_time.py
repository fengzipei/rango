# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lanunion', '0009_auto_20171101_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='review_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date reviewed'),
        ),
    ]
