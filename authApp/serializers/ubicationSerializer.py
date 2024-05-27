from rest_framework import serializers
from authApp.models.ubication import Ubication

class UbicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubication
        fields = [
            'ubication_id',
            'country',
            'department',
            'city',
            'neighborthood',
            'address',
            'postal_code',
            'location',
            'active'
        ]

        read_only_fields = [
            'ubication_id',
        ]

        def validate(self, data):
            if len(data.get('country', '')) > 30:
                raise serializers.ValidationError("The 'country' field cannot exceed 100 characters.")
            if len(data.get('department', '')) > 100:
                raise serializers.ValidationError("The 'department' field cannot exceed 100 characters.")
            if len(data.get('neighborthood', '')) > 100:
                raise serializers.ValidationError("The 'neighborthood' field cannot exceed 100 characters.")
            if len(data.get('address', '')) > 200:
                raise serializers.ValidationError("The 'address' field cannot exceed 200 characters.")
            if len(data.get('posta_code', '')) > 20:
                raise serializers.ValidationError("The 'postal code' field cannot exceed 20 characters.")
            return data