# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 03:10
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('lanunion', '0012_auto_20171101_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 3, 10, 53, 571601, tzinfo=utc),
                                       verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='application',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 3, 10, 53, 572161, tzinfo=utc),
                                       verbose_name='data created'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 3, 10, 53, 572708, tzinfo=utc),
                                       verbose_name='data published'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 3, 10, 53, 570392, tzinfo=utc),
                                       verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='repairorder',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 3, 10, 53, 570903, tzinfo=utc),
                                       verbose_name='date created'),
        ),
    ]
