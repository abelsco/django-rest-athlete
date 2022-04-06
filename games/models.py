from django.db import models

class Games(models.Model):
    slug = models.SlugField(primary_key=True, default='')
    name = models.CharField(max_length=13, null=True)
    year = models.IntegerField()
    season = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    class Meta:
        ordering = ('-slug',)

    def __str__(self):
        return self.name


# Create your models here.
