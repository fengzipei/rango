# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lanunion', '0007_repairorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('waiting for auditing', 'waiting for auditing'), ('accepted', 'accepted'),
                                            ('rejected', 'rejected')],
                                   default=('waiting for auditing', 'waiting for auditing'), max_length=50),
        ),
    ]
