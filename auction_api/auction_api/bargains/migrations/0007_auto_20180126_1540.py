# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 09:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrative_division', '0002_auto_20180126_1457'),
        ('bargains', '0006_auto_20180126_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='BargainAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administrative_division.AdministrativeDivision')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BargainComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='bargainbet',
            name='participant',
        ),
        migrations.AlterField(
            model_name='bargain',
            name='participants',
            field=models.ManyToManyField(related_name='bargains', through='bargains.BargainBet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bargaincomment',
            name='bargain',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bargains.Bargain'),
        ),
        migrations.AddField(
            model_name='bargaincomment',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bargains_bargaincomment_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bargaincomment',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bargainaddress',
            name='bargain',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bargains.Bargain'),
        ),
        migrations.AddField(
            model_name='bargainaddress',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bargains_bargainaddress_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bargainaddress',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bargain',
            name='addresses',
            field=models.ManyToManyField(through='bargains.BargainAddress', to='administrative_division.AdministrativeDivision'),
        ),
        migrations.AddField(
            model_name='bargain',
            name='comments',
            field=models.ManyToManyField(related_name='bargain_comments', through='bargains.BargainComment', to=settings.AUTH_USER_MODEL),
        ),
    ]
