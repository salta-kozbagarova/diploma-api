# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-23 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0016_auto_20180123_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
