# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-26 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20180626_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
