from django.db import models
from noc.models import Noc

class Athlete(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    age = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    team = models.CharField(max_length=60)
    noc = models.ForeignKey(Noc, related_name='noc_name', to_field='name', on_delete=models.CASCADE, default='')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
    

# Create your models here.
