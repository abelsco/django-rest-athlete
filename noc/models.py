from django.db import models


class Noc(models.Model):
    name = models.CharField(max_length=3)
    region = models.CharField(max_length=60)
    notes = models.TextField()

    def __str__(self):
        return self.name
