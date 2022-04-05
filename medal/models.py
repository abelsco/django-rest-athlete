from tkinter import CASCADE
from django.db import models
from event.models import Event
from athlete.models import Athlete

class Medal(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    medal = models.CharField(max_length=6)

    def __str__(self):
        return self.medal
    

# Create your models here.
