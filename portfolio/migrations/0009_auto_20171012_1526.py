# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-12 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20171012_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='num_views',
            field=models.IntegerField(default=0, verbose_name='Views Number'),
        ),
    ]
