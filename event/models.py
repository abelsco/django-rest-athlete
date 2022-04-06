from django.db import models
from django.utils.timezone import datetime

class Event(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True, default='')
    name = models.CharField(max_length=255, null=True)
    sport = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('-slug', )

    def __str__(self):
        return self.name

# Create your models here.
