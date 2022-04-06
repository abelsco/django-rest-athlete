from rest_framework import serializers
from .models import Games

class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'