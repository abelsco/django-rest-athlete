from tkinter import CASCADE
from django.db import models
from noc.models import Noc

class Athlete(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    height = models.CharField(max_length=3)
    weight = models.CharField(max_length=5)
    team = models.CharField(max_length=60)
    noc = models.ForeignKey(Noc,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# Create your models here.
