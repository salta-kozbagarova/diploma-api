# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-21 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bargains', '0025_auto_20180202_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bargain',
            name='current_price',
            field=models.IntegerField(verbose_name='Current Price'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='start_price',
            field=models.IntegerField(verbose_name='Start Price'),
        ),
    ]