# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-12 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170925_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_views',
            field=models.IntegerField(default=0, help_text='(views number)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
