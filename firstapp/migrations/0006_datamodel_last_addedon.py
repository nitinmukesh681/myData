# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20180809_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodel',
            name='last_addedOn',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]