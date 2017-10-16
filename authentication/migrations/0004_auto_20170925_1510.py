# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-25 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20170925_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, help_text='(optional)', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, help_text='(will be automatically generated)', null=True, unique=True),
        ),
    ]
