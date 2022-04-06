from django.contrib import admin
from .models import Medal

@admin.register(Medal)
class MedalAdmin(admin.ModelAdmin):
    list_display = ('id', 'athlete', 'games', 'event', 'medal')

# Register your models here.
