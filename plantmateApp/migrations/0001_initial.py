# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-12 03:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=128, unique=True)),
                ('lat', models.CharField(max_length=20)),
                ('long', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('latin_name', models.CharField(max_length=128, unique=True)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='Small', max_length=128)),
                ('characteristics', models.CharField(max_length=128)),
                ('climate', models.CharField(choices=[('cool', 'Cool'), ('warm', 'Warm')], default='cool', max_length=128)),
                ('light', models.CharField(choices=[('sunny', 'Sunny'), ('shady', 'Shady')], default='sunny', max_length=128)),
                ('room', models.CharField(choices=[('Living-room/Bedroom', 'living-room/bedroom'), ('Kitchen/Bathroom', 'kitchen/bathroom')], default='Living-room/Bedroom', max_length=128)),
                ('pet', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('url', models.URLField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='main_plant_images')),
            ],
            options={
                'verbose_name_plural': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='plant_images')),
                ('plant_name', models.CharField(default=' ', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSavedPlants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_plant', models.CharField(default=' ', max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWishlistPlants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishlist_plant', models.CharField(default=' ', max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantmateApp.Plant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantmateApp.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='userwishlistplants',
            unique_together=set([('wishlist_plant', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='usersavedplants',
            unique_together=set([('saved_plant', 'user')]),
        ),
    ]
