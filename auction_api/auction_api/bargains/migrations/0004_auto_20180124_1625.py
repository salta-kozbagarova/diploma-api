# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bargains', '0003_auto_20180124_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bargain',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bargains_bargain_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bargainproducts',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bargains_bargainproducts_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bargainproducts',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bargains_bargaintype_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
