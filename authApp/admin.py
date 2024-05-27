from django.contrib import admin

from .models.user import User
from .models.role import Role
from .models.permission import Permission

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)

# Register your models here.
