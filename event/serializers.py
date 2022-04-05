from dataclasses import fields
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'sport', 'games']