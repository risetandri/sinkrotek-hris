from rest_framework import serializers
from core.infrastructure.models.employee import EmployeeModel
from .auth import AuthSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    auth = AuthSerializer()

    class Meta:
        model = EmployeeModel
        fields = '__all__'