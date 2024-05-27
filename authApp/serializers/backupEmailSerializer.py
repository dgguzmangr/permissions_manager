from rest_framework import serializers
from authApp.models.backupEmail import BackupEmail

class BackupEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupEmail
        fields = [
            'backup_email_id',
            'email',
            'active'
        ]

        read_only_fields = [
            'backup_email_id'
        ]

        def validate(self, data):
            if len(data.get('email', '')) > 100:
                raise serializers.ValidationError("The 'email' field cannot exceed 100 characters.")
            return data