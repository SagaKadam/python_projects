from dataclasses import field
from statistics import mode
from rest_framework import serializers
from . import models

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notes
        fields = '__all__'
