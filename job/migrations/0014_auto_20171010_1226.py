# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-10 10:26
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20171010_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=froala_editor.fields.FroalaField(help_text='(job description)'),
        ),
    ]
