from .models import Medal
from rest_framework import serializers

class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medal
        fields = '__all__'