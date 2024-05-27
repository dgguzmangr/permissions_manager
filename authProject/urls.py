"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) # comentar par deshabilitar seguridad
from rest_framework.authtoken import views
from authApp.views import appView
from authApp.views import businessModelView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for Product Manager",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # User API
    # path('show-users/', UserController.show_users, name='List all created users'),
    # path('create-user/', UserController.create_user, name='Create a new user'),
    # path('update-user/<int:pk>/', UserController.update_user, name='Update a selected user'),
    # path('delete-user/<int:pk>/', UserController.delete_user, name='Delete a selected user'),
    #login
    # path('login/', UserController.login),

    # User API
    path('show-users/', appView.show_users, name='List all created users'),
    path('create-user/', appView.create_user, name='Create a new user'),
    path('update-user/<int:pk>/', appView.update_user, name='Update a selected user'),
    path('partial-update-user/<int:pk>/', appView.partial_update_user, name='Update a selected attribute for a user'),
    path('delete-user/<int:pk>/', appView.delete_user, name='Delete a selected user'),

    # Role API
    path('show-roles/', appView.show_roles, name='List all created roles'),
    path('create-role/', appView.create_role, name='Create a new role'),
    path('update-role/<int:pk>/', appView.update_role, name='Update a selected role'),
    path('partial-update-role/<int:pk>/', appView.partial_update_role, name='Update a selected attribute for a role'),
    path('delete-role/<int:pk>/', appView.delete_role, name='Delete a selected role'),

    # Permission API
    path('show-permissions/', appView.show_permissions, name='List all created permits'),
    path('create-permissions/', appView.create_permission, name='Create a new permit'),
    path('update-permission/<int:pk>/', appView.update_permission, name='Update a selected permit'),
    path('partial-update-permission/<int:pk>/', appView.partial_update_permission, name='Update a selected attribute for a permission'),
    path('delete-permission/<int:pk>/', appView.delete_permission, name='Delete a selected permit'),

    # BackupEmail API
    path('show-backup-email/', appView.show_backupEmail, name='List all created backup emails'),
    path('create-backup-email/', appView.create_backupEmail, name='Create a new backup email'),
    path('update-backup-email/<int:pk>/', appView.update_backupEmail, name='Update a selected backup email'),
    path('partial-update-backup-email/<int:pk>/', appView.partial_update_backupEmail, name='Update a selected attribute for a backup email'),
    path('delete-backup-email/<int:pk>/', appView.delete_backupEmail, name='Delete a selected backup email'),

    # Phone API
    path('show-backup-phone/', appView.show_phone, name='List all created backup phones'),
    path('create-phone/', appView.create_phone, name='Create a new phone'),
    path('update-phone/<int:pk>/', appView.update_phone, name='Update a selected phone'),
    path('partial-update-phone/<int:pk>/', appView.partial_update_phone, name='Update a selected attribute for a phone'),
    path('delete-phone/<int:pk>/', appView.delete_phone, name='Delete a selected phone'),

    # Business Model url
    path('field-structure-view/', businessModelView.field_structure_view, name='Generate a json structure for all models'),

    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/swagger/
