from django.contrib import admin

from .models.role import Role
from .models.permission import Permission

admin.site.register(Role)
admin.site.register(Permission)

# Register your models here.
