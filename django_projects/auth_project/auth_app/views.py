from django.shortcuts import render
from .models import Auth
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AuthView(viewsets.ModelViewSet):
    http_method_names =['get']
    serializer_class = Auth
    permission_classes = (IsAuthenticated,)
    filer_backends = [filters.OrderingFilter]
    ordering_fileds = ['updated']
    ordering = ['-updated']
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Auth.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]
        obj = Auth.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)
        return obj

    