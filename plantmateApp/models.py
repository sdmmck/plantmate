from django.db import models
from django.template.defaultfilters import slugify


class Business (models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Business, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.name
