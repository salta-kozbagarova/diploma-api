# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('author', models.CharField(max_length=255)),
                ('published', models.DateField()),
                ('material', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('products.product', models.Model),
        ),
    ]
