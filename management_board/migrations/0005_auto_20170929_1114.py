# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-29 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_board', '0004_auto_20170929_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillsmember',
            options={'verbose_name_plural': 'Skills Member'},
        ),
        migrations.AlterField(
            model_name='skillsmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='management_board.BoardMember'),
        ),
    ]
