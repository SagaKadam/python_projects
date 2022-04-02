from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
class NotesList(generics.ListAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer 

class NotesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer 
