# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180130_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bargain',
        ),
    ]
