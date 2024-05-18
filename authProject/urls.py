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

    # Role API
    path('show-roles/', appView.show_roles),
    path('create-role/', appView.create_role),
    path('update-role/<int:pk>/', appView.update_role),
    path('delete-role/<int:pk>/', appView.delete_role),

    # Permission API
    path('show-permissions/', appView.show_permissions),
    path('create-permissions/', appView.create_permission),
    path('update-permission/<int:pk>/', appView.update_permission),
    path('delete-permission/<int:pk>/', appView.delete_permission),

    # Rol and permissions API
    path('user-rol-list/', appView.user_role_list),                 # assign roles to users
    path('role-permission-list/', appView.role_permission_list),    # assign permissions to roles
    path('check-permission/', appView.check_permission),            # check permissions

# Business Model url
    path('field-structure-view/', businessModelView.field_structure_view),


    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/swagger/
