# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-12 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_num_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='num_views',
            field=models.IntegerField(default=0, help_text='(views number)', verbose_name='Visitors Number'),
        ),
    ]
