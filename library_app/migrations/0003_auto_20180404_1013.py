# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_auto_20180404_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]