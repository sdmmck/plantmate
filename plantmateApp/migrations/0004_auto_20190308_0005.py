# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-08 00:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plantmateApp', '0003_auto_20190307_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwishlistplants',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userwishlistplants',
            unique_together=set([('wishlist_plant', 'user')]),
        ),
    ]