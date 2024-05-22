from django.db import models

class UserRole(models.Model):
    userRole_id = models.AutoField(primary_key=True)
    assigned_at = models.DateTimeField('Assigned at', auto_now_add=True)
