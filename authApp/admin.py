from django.contrib import admin

from .models.user import User
from .models.role import Role
from .models.permission import Permission
from .models.backupEmail import BackupEmail
from .models.phone import Phone
from .models.ubication import Ubication

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(BackupEmail)
admin.site.register(Phone)
admin.site.register(Ubication)

# Register your models here.
