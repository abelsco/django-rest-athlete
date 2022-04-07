from django.shortcuts import render
from .models import Medal
from .serializers import MedalSerializer
from rest_framework import viewsets

class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer

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
