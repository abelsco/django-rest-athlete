from django.db import models
from django.utils.timezone import datetime


class Noc(models.Model):
    name = models.CharField(max_length=3, primary_key=True)
    region = models.CharField(max_length=60)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
