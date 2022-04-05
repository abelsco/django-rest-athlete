from django.db import models

class Games(models.Model):
    name = models.CharField(max_length=13)
    year = models.IntegerField()
    season = models.CharField(max_length=6)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.
