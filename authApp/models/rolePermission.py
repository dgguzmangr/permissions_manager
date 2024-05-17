from django.db import models
from .role import Role
from .permission import Permission

class RolePermission(models.Model):
    rolePermission_id = models.AutoField(primary_key=True)
    assigned_at = models.DateTimeField('Assigned at', auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='rolePermission')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='rolePermission')