from django.shortcuts import render
from .models import Athlete
from .serializers import AthleteSerializer
from rest_framework import viewsets, generics, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

class AthleteViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()

    def get(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)

    def options(self, request, *args, **kwargs):
        return super().options(request, *args, **kwargs)
    
    def get_queryset(self):
        return super().get_queryset()
    



# Create your views here.
