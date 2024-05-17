from rest_framework import serializers
from authApp.models.rolePermission import RolePermission

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = [
            'rolePermission_id',
            'assigned_at',
            'role',
            'permission'
        ]

        read_only_fields = [
            'rolePermission',
            'assigned_at'
        ]