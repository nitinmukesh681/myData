# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_addasearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='addasearch',
            name='fieldType',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
