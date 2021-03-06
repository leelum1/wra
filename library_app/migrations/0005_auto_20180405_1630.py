# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-05 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_auto_20180404_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bar_code',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='call_no',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Unavailable', 'Unavailable'), ('Reference', 'Reference')], max_length=80, null=True),
        ),
    ]
