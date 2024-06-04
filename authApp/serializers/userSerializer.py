from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from authApp.models.user import User
from authApp.serializers.groupSerializer import GroupSerializer
from authApp.serializers.permissionSerializer import PermissionSerializer

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'type',
            'company_name',
            'name',
            'last_name',
            'document',
            'nit',
            'email',
            'username',
            'password',
            'status',
            'user_groups',
            'backupEmail',
            'phone',
            'ubication',
            'groups',
            'user_permissions',
        ]

        read_only_fields = [
            'user_id',
            'username'
        ]

    def validate(self, data):
        if len(data.get('company_name', '')) > 100:
            raise serializers.ValidationError("The 'company_name' field cannot exceed 100 characters.")
        if len(data.get('name', '')) > 100:
            raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
        if len(data.get('last_name', '')) > 100:
            raise serializers.ValidationError("The 'last_name' field cannot exceed 100 characters.")
        if len(data.get('document', '')) > 15:
            raise serializers.ValidationError("The 'document' field cannot exceed 15 characters.")
        if len(data.get('nit', '')) > 18:
            raise serializers.ValidationError("The 'nit' field cannot exceed 18 characters.")
        if len(data.get('email', '')) > 100:
            raise serializers.ValidationError("The 'email' field cannot exceed 100 characters.")
        if len(data.get('password', '')) > 128:
            raise serializers.ValidationError("The 'password' field cannot exceed 128 characters.")
        return data

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user_permissions_data = validated_data.pop('user_permissions', [])
        user_groups_data = validated_data.pop('user_groups', [])
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Asignar grupos
        groups = []
        for group_data in groups_data:
            group, created = Group.objects.get_or_create(name=group_data['name'])
            groups.append(group)

            for permission_data in group_data.get('permissions', []):
                permission, created = Permission.objects.get_or_create(name=permission_data['name'])
                group.permissions.add(permission)
        user.groups.set(groups)

        # Asignar permisos de usuario
        permissions = []
        for permission_data in user_permissions_data:
            permission, created = Permission.objects.get_or_create(name=permission_data['name'])
            permissions.append(permission)
        user.user_permissions.set(permissions)

        # Asignar user_groups
        user.user_groups.set(user_groups_data)

        return user

    def update(self, instance, validated_data):
        groups_data = validated_data.pop('groups', None)
        user_permissions_data = validated_data.pop('user_permissions', None)
        user_groups_data = validated_data.pop('user_groups', None)
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()

        if groups_data is not None:
            groups = []
            for group_data in groups_data:
                group, created = Group.objects.get_or_create(name=group_data['name'])
                groups.append(group)

                for permission_data in group_data.get('permissions', []):
                    permission, created = Permission.objects.get_or_create(name=permission_data['name'])
                    group.permissions.add(permission)
            instance.groups.set(groups)

        if user_permissions_data is not None:
            permissions = []
            for permission_data in user_permissions_data:
                permission, created = Permission.objects.get_or_create(name=permission_data['name'])
                permissions.append(permission)
            instance.user_permissions.set(permissions)

        if user_groups_data is not None:
            instance.user_groups.set(user_groups_data)

        return instance
