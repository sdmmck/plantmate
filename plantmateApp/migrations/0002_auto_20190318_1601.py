# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantmateApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=' ', verbose_name='date published'),
        ),
    ]