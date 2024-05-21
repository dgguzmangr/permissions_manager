from django.contrib import admin

from .models.user import User
from .models.role import Role
from .models.permission import Permission
from .models.userRole import UserRole
from .models.rolePermission import RolePermission

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)
admin.site.register(RolePermission)

# Register your models here.
