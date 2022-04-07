from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NocSerializer
from .models import Noc


# ViewSets define the view behavior.
class NocViewSet(viewsets.ModelViewSet):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer

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
