# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_useraddress_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_userphone_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
