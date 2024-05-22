from rest_framework import serializers
from authApp.models.userRole import UserRole

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = [
            'userRole_id',
            'assigned_at'
        ]

        read_only_fields = [
            'userRole_id',
            'assigned_at'
        ]