from django.db import models


class Noc(models.Model):
    name = models.CharField(max_length=3, primary_key=True)
    region = models.CharField(max_length=60)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
