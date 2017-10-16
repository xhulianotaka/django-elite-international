# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-27 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20170927_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('current_company', models.CharField(blank=True, help_text='(optional)', max_length=300, null=True)),
                ('portfolio_url', models.URLField(blank=True, help_text='optional', null=True)),
                ('additional_information', models.TextField(blank=True, help_text='add a cover letter or anything else you want to share', null=True)),
                ('resume', models.FileField(help_text='resume/CV', upload_to='Application_Documents')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
            ],
        ),
    ]
