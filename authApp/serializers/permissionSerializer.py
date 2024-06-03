from rest_framework import serializers
# from authApp.models.permission import Permission
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            'id',
            'name',
            'codename'
        ]

        read_only_fields = [
            'id'
        ]