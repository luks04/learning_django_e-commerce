from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all() # Query for get all objects
    serializer_class = MovieSerializer

'''
class <ClassName>ViewSet(viewsets.ModelViewSet):
    queryset = <ClassName>.objects.all() # Query for get all objects
    serializer_class = <ClassName>Serializer # Import it
'''
