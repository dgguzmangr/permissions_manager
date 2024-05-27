from django.db import models

class BackupEmail(models.Model):
    backup_email_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authApp'