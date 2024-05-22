from django.db import models
from .permission import Permission

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    description = models.CharField('Description', max_length=100, blank=False, null=False)
    permission = models.ManyToManyField(Permission, related_name='permissions')

    class Meta:
        app_label = 'authApp'