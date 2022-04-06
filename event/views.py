from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()[:10]
    serializer_class =  EventSerializer


# Create your views here.
