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


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
