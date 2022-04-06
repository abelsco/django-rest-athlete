from tkinter import CASCADE
from django.db import models
from event.models import Event
from athlete.models import Athlete
from games.models import Games

class Medal(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='event_name', to_field='name', on_delete=models.CASCADE, default='')
    games = models.ForeignKey(Games, related_name='games_name', to_field='name', on_delete=models.CASCADE, default='')
    medal = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.medal
    

# Create your models here.
