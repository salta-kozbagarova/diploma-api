# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_auto_20180126_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jeans',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('material', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('products.product', models.Model),
        ),
    ]
