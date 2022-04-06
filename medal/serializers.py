from .models import Medal
from rest_framework import serializers

class MedalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medal
        fields = ['athlete', 'games', 'event', 'medal']