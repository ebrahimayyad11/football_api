from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Football
from .serializer import FootballSerializer

# Create your views here.
class FootballListView(generics.ListCreateAPIView):    
    serializer_class = FootballSerializer
    queryset = Football.objects.all()

class FootballDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FootballSerializer
    queryset = Football.objects.all()