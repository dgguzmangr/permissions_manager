from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
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
            'role',
            'backupEmail',
            'phone',
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

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user

        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            if password:
                instance.set_password(password)
            instance.save()
            return instance