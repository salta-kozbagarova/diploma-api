# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 05:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bargains', '0013_auto_20180129_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bargain',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 5, 41, 53, 919000, tzinfo=utc), verbose_name='End Date'),
        ),
    ]