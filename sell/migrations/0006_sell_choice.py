# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0005_sell_buy_it_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='choice',
            field=models.CharField(choices=[('1', 'Locomotive'), ('2', 'Engine'), ('3', 'Track'), ('4', 'All')], default=0, max_length=15),
        ),
    ]