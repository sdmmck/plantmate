from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Business (models.Model):
    name = models.CharField(max_length=128, unique=True)
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Plant, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
