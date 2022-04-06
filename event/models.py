from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    sport = models.CharField(max_length=30)
    slug_id = models.IntegerField(null=True)

    class Meta:
        ordering = ('-slug_id', )

    def __str__(self):
        return self.name



# Create your models here.
