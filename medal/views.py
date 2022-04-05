from django.shortcuts import render
from .models import Medal
from .serializers import MedalSerializer
from rest_framework import viewsets

class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer

# Create your views here.
