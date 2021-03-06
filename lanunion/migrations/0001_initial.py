# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 06:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('application_time', models.DateTimeField(verbose_name='data created')),
                ('reason', models.CharField(max_length=500)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('review_time', models.DateTimeField(blank=True, null=True, verbose_name='date audited')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('publish_time', models.DateTimeField(verbose_name='data published')),
                ('content', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(
                    choices=[('student', 'student'), ('super admin', 'super admin'), ('normal admin', 'normal admin'),
                             ('repairer', 'repairer'), ('teacher', 'teacher')], max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('join_time', models.DateTimeField(verbose_name='date joined')),
                ('exit_time', models.DateTimeField(blank=True, null=True, verbose_name='date leave')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RepairOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_text', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField(verbose_name='date created')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='date finished')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('applicant_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_id',
                                   to='lanunion.Profile')),
                ('repairer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='repairer_id', to='lanunion.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='pubisher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher_id',
                                    to='lanunion.Profile'),
        ),
        migrations.AddField(
            model_name='applications',
            name='applicant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newbie_id',
                                    to='lanunion.Profile'),
        ),
        migrations.AddField(
            model_name='applications',
            name='reviewer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='reviewer_id', to='lanunion.Profile'),
        ),
        migrations.AddField(
            model_name='advices',
            name='suggester_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanunion.Profile'),
        ),
    ]
