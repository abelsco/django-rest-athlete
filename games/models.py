from django.db import models
from django.utils.timezone import datetime

class Games(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True)
    name = models.CharField(max_length=13, null=True)
    year = models.IntegerField()
    season = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('-slug',)

    def __str__(self):
        return self.name


# Create your models here.
