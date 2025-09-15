from rest_framework import serializers
from core.infrastructure.models.auth import AuthModel

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthModel
        fields = '__all__'
