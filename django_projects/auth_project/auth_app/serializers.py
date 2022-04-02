from auth_app.models import Auth
from rest_framework import serializers

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ['id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_fields = ['is_active', 'created', 'updated']