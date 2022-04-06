from django.shortcuts import render
from .models import Athlete
from .serializers import AthleteSerializer
from rest_framework import viewsets

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()[:10]
    serializer_class = AthleteSerializer

# Create your views here.
