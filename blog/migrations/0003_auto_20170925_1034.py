# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-25 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170925_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, help_text='will be automatically generated', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=None, help_text='will be automatically generated', unique=True),
            preserve_default=False,
        ),
    ]
