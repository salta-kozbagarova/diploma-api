# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 06:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_division', '0003_auto_20180130_1428'),
        ('users', '0004_auto_20180130_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(through='users.UserAddress', to='administrative_division.AdministrativeDivision'),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='phonenumbers', to=settings.AUTH_USER_MODEL),
        ),
    ]