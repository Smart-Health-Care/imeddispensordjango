# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-19 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_medicine_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='otc',
            field=models.BooleanField(default=False),
        ),
    ]
