from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Business (models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128, unique=True)
    lat = models.CharField(max_length=20, unique=False)
    long = models.CharField(max_length=20, unique=False)
    url = models.URLField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Business, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.name


class Plant (models.Model):
    size_choices = (("small", "Small"), ("medium", "Medium"), ("large", "Large"))
    climate_choices = (("cool", "Cool"), ("warm", "Warm"))
    light_choices = (("sunny", "Sunny"), ("shady", "Shady"))
    room_choices = (("Living-room/Bedroom", "living-room/bedroom"), ("Kitchen/Bathroom", "kitchen/bathroom"))

    name = models.CharField(max_length=128, unique=True)
    latin_name = models.CharField(max_length=128, unique=True)
    size = models.CharField(max_length=128, unique=False,  blank=False, default="Small", choices=size_choices)
    characteristics = models.CharField(max_length=128, unique=False)
    climate = models.CharField(max_length=128, unique=False, blank=False, default="cool", choices=climate_choices)
    light = models.CharField(max_length=128, unique=False, blank=False, default="sunny", choices=light_choices)
    room = models.CharField(max_length=128, unique=False, blank=False, default="Living-room/Bedroom", choices=room_choices)
    pet = models.CharField(max_length=128, unique=False)
    slug = models.SlugField()
    url = models.URLField()
    picture = models.ImageField(upload_to='main_plant_images', blank=True, null=True)
    #DESCRIPTION UNIQUE NEEDS TO BE CHANGED TO TRUE AND BLANK TO FALSE WHEN REAL DESCRIPTIONS ADDED
    description = models.TextField(unique=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Plant, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.name


class PlantImage (models.Model):
    picture = models.ImageField(upload_to='plant_images', blank=True, null=True)
    plant_name = models.CharField(max_length=128, unique=False, default=" ")

    def save(self, *args, **kwargs):
        super(PlantImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.plant_name


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class UserSavedPlants(models.Model):
    class Meta:
        unique_together = ('saved_plant', 'user')

    user = models.ForeignKey(User)
    saved_plant = models.CharField(max_length=128, unique=False, default=" ")

    def save(self, *args, **kwargs):
        super(UserSavedPlants, self).save(*args, **kwargs)

    def __str__(self):
        return self.saved_plant


class UserWishlistPlants(models.Model):
    class Meta:
        unique_together = ('wishlist_plant', 'user')

    user = models.ForeignKey(User)
    wishlist_plant = models.CharField(max_length=128, unique=False, default=" ")

    def save(self, *args, **kwargs):
        super(UserWishlistPlants, self).save(*args, **kwargs)

    def __str__(self):
        return self.wishlist_plant


class Comment(models.Model):
    user = models.ForeignKey(User)
    plant = models.ForeignKey(Plant)
    plant_slug = models.CharField(max_length=128)
    body = models.TextField(unique=False, default=" ")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.body
