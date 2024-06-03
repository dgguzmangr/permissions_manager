from rest_framework import serializers
from django.contrib.auth.models import  Group
from authApp.serializers.permissionSerializer import PermissionSerializer

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']