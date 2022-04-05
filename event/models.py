from django.db import models
from games.models import Games

class Event(models.Model):
    name = models.CharField(max_length=60)
    sport = models.CharField(max_length=30)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
