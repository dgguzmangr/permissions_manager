from rest_framework import serializers
from authApp.models.permission import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            'permission_id',
            'name',
            'description'
        ]

        read_only_fields = [
            'permission_id'
        ]

        def validate(self, data):
            if len(data.get('name', '')) > 100:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            if len(data.get('description', '')) > 100:
                raise serializers.ValidationError("The 'description' field cannot exceed 100 characters.")
            return data