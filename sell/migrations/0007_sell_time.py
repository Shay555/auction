# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0006_sell_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='time',
            field=models.CharField(choices=[('1', '1 weak'), ('2', '2 weaks'), ('3', '3 weaks')], default=0, max_length=10),
        ),
    ]
