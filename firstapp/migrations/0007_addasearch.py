# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_datamodel_last_addedon'),
    ]

    operations = [
        migrations.CreateModel(
            name='addAsearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldIs', models.CharField(blank=True, max_length=55, null=True)),
            ],
        ),
    ]
