from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GamesSerializer
from .models import Games


# ViewSets define the view behavior.
class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer    

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
