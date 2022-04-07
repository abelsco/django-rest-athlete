from django.contrib import admin
from .models import Athlete

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team', 'noc')

# Register your models here.
