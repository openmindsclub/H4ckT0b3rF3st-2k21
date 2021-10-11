from django.shortcuts import render
from rest_framework import viewsets
from .models import Series
from .serializers import SeriesSerializer

# Create your views here.

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
