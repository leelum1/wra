# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-22 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservoir_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caroni',
            name='pumpRelease',
        ),
        migrations.AddField(
            model_name='caroni',
            name='pump',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caroni',
            name='release',
            field=models.FloatField(blank=True, null=True),
        ),
    ]