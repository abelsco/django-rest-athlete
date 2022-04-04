from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NocSerializer
from .models import Noc


# ViewSets define the view behavior.
class NocViewSet(viewsets.ModelViewSet):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer

# Create your views here.
