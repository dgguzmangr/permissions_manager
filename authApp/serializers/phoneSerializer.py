from rest_framework import serializers
from authApp.models.phone import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = [
            'phone_id',
            'phone_number',
            'active'
        ]

        read_only_fields = [
            'phone_id',
        ]

        def validate_phone_number(self, value):
            if not value:
                raise serializers.ValidationError("The phone number cannot be null.")
            return value