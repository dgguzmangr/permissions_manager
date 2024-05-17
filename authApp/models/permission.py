from django.db import models

class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    description = models.CharField('Name', max_length=100, blank=False, null=False)

    class Meta:
        app_label = 'authApp'