from django.db import models
from django.utils.text import slugify

class Games(models.Model):
    name = models.CharField(max_length=13, primary_key=True)
    year = models.IntegerField()
    season = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    slug_id = models.IntegerField(null=True)

    class Meta:
        ordering = ('-slug_id',)

    def __str__(self):
        return self.name


# Create your models here.
