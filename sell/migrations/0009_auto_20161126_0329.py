# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0008_sell_remaining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='title',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
