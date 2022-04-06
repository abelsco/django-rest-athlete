from django.contrib import admin
from .models import Games

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'season', 'city')

# Register your models here.
