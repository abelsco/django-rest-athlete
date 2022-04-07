from django.contrib import admin
from .models import Noc

@admin.register(Noc)
class NocAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'notes')
# Register your models here.
