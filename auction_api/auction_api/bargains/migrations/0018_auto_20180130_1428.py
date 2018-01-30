# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 08:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_division', '0003_auto_20180130_1428'),
        ('bargains', '0017_auto_20180129_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bargainaddress',
            name='address',
        ),
        migrations.RemoveField(
            model_name='bargainaddress',
            name='bargain',
        ),
        migrations.RemoveField(
            model_name='bargainaddress',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='bargainaddress',
            name='updated_by',
        ),
        migrations.AlterModelOptions(
            name='bargaintype',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='bargain',
            name='addresses',
        ),
        migrations.AddField(
            model_name='bargain',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bargain_addresses', to='administrative_division.AdministrativeDivision'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 8, 28, 42, 675400, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='bargainbet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='bargainbet',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='bargainbet',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted'),
        ),
        migrations.AlterField(
            model_name='bargainbet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='bargaincomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='bargaincomment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='bargaincomment',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted'),
        ),
        migrations.AlterField(
            model_name='bargaincomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Deleted'),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.DeleteModel(
            name='BargainAddress',
        ),
    ]
