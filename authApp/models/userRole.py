from django.db import models
from .role import Role

class UserRole(models.Model):
    userRole_id = models.AutoField(primary_key=True)
    assigned_at = models.DateTimeField('Assigned at', auto_now_add=True)
    user = models.IntegerField('User', blank=False, null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='userRole')
