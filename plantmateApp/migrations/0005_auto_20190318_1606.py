# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plantmateApp', '0004_auto_20190318_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 16, 6, 6, 583857, tzinfo=utc), verbose_name='date published'),
        ),
    ]