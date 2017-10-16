# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-27 13:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(help_text='(will be automatically generated)', unique=True)),
                ('description', models.TextField(help_text='job description')),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(help_text='(job location)', max_length=300)),
                ('company_name', models.CharField(max_length=250)),
                ('last_date', models.DateField(help_text='last day of application')),
                ('requirements', models.TextField(help_text='job requirements')),
            ],
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='slug',
            field=models.SlugField(help_text='(will be automatically generated)', unique=True),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobCategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
