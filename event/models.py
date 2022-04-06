from django.db import models

class Event(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True, default='')
    name = models.CharField(max_length=255, null=True)
    sport = models.CharField(max_length=30)

    class Meta:
        ordering = ('-slug', )

    def __str__(self):
        return self.name

# Create your models here.
