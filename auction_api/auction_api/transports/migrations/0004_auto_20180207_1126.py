# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bargains', '0025_auto_20180202_1241'),
        ('products', '0007_remove_product_bargain'),
        ('transports', '0003_auto_20180207_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='product_ptr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='transport_ptr',
        ),
        migrations.AddField(
            model_name='car',
            name='product_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
    ]