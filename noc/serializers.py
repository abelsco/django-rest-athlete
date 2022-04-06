from statistics import mode
from rest_framework import serializers
from .models import Noc

class NocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noc
        fields = ['name', 'region', 'notes']