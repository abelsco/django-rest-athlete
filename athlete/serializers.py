from rest_framework import serializers
from .models import Athlete

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ['id', 'name', 'sex', 'age', 'height', 'weight', 'team', 'noc']