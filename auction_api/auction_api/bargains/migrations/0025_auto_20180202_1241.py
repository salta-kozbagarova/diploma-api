# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bargains', '0024_bargain_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bargain',
            name='product',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]