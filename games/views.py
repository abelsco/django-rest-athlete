from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GamesSerializer
from .models import Games


# ViewSets define the view behavior.
class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

# Create your views here.
