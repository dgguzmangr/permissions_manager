from rest_framework import serializers
from authApp.models.role import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'role_id',
            'name',
            'description',
            'permission'
        ]

        read_only_fields = [
            'role_id'
        ]

        def validate(self, data):
            if len(data.get('name', '')) > 100:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            if len(data.get('description', '')) > 100:
                raise serializers.ValidationError("The 'description' field cannot exceed 100 characters.")
            return data