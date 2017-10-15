# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
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
                ('audit_time', models.DateTimeField(blank=True, null=True, verbose_name='date audited')),
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
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('category', models.CharField(
                    choices=[('student', 'student'), ('super admin', 'super admin'), ('normal admin', 'normal admin'),
                             ('repairer', 'repairer'), ('teacher', 'teacher')], max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('join_time', models.DateTimeField(verbose_name='date joined')),
                ('exit_time', models.DateTimeField(blank=True, null=True, verbose_name='date leave')),
            ],
        ),
        migrations.AddField(
            model_name='repairorder',
            name='applicant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_id',
                                    to='lanunion.Staff'),
        ),
        migrations.AddField(
            model_name='repairorder',
            name='repairer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='repairer_id', to='lanunion.Staff'),
        ),
        migrations.AddField(
            model_name='applications',
            name='applicant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newbie_id',
                                    to='lanunion.Staff'),
        ),
        migrations.AddField(
            model_name='applications',
            name='auditor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='auditor_id', to='lanunion.Staff'),
        ),
        migrations.AddField(
            model_name='advices',
            name='suggester_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanunion.Staff'),
        ),
    ]