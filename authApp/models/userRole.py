from django.db import models
from .user import User
from .role import Role

class UserRole(models.Model):
    userRole_id = models.AutoField(primary_key=True)
    assigned_at = models.DateTimeField('Assigned at', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserRole')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='userRole')
