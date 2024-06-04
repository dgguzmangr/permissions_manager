from rest_framework import serializers
from django.contrib.auth.models import  Group, Permission
from authApp.serializers.permissionSerializer import PermissionSerializer

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        group = Group.objects.create(**validated_data)
        for permission_data in permissions_data:
            permission, created = Permission.objects.get_or_create(**permission_data)
            group.permissions.add(permission)
        return group

    def update(self, instance, validated_data):
        permissions_data = validated_data.pop('permissions', None)
        if permissions_data:
            instance.permissions.clear()
            for permission_data in permissions_data:
                permission, created = Permission.objects.get_or_create(**permission_data)
                instance.permissions.add(permission)

        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance