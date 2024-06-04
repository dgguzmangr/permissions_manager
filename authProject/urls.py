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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) # comentar par deshabilitar seguridad
from rest_framework.authtoken import views
from authApp.views import appView, businessModelView, apiGatewayView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authApp.custom_swagger import CustomSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="WMS API Gateway",
        default_version='v1',
        description="API for users and permissions Manager",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomSchemaGenerator,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # User API
    path('show-users/', appView.show_users, name='List all created users'),
    path('create-user/', appView.create_user, name='Create a new user'),
    path('update-user/<int:pk>/', appView.update_user, name='Update a selected user'),
    path('partial-update-user/<int:pk>/', appView.partial_update_user, name='Update a selected attribute for a user'),
    path('delete-user/<int:pk>/', appView.delete_user, name='Delete a selected user'),

    # Group API
    path('show-groups/', appView.show_groups, name='List all created groups'),
    path('create-group/', appView.create_group, name='Create a new role'),
    path('update-group/<int:pk>/', appView.update_group, name='Update a selected group'),
    path('partial-update-group/<int:pk>/', appView.partial_update_group, name='Update a selected attribute for a group'),
    path('delete-group/<int:pk>/', appView.delete_group, name='Delete a selected group'),
    path('assign-group-to-user/', appView.assign_group_to_user, name='Assign group to user'),

    # Permission API
    path('show-permissions/', appView.show_permissions, name='List all created permits'),
    path('assign-permission-to-group/', appView.assign_permission_to_group, name='Assign permission to group'),

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

    # Ubication API
    path('show-ubications/', appView.show_ubication, name='List all created ubications'),
    path('create-ubication/', appView.create_ubication, name='Create a new ubication'),
    path('update-ubication/<int:pk>/', appView.update_ubication, name='Update a selected ubication'),
    path('partial-update-ubication/<int:pk>/', appView.partial_update_ubication, name='Update a selected attribute for an ubication'),
    path('delete-ubication/<int:pk>/', appView.delete_ubication, name='Delete a selected ubication'),

    # Business Model url
    path('permissions-manager-field-structure/', businessModelView.permissions_field_structure_view, name='Generate a json structure for all models'),
    path('products-manager-field-structure/', apiGatewayView.products_field_structure_view, name='Generate a json structure for all models'),
    path('warehouses-manager-field-structure/', apiGatewayView.warehouses_field_structure_view, name='Generate a json structure for all models'),

    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),

    # API Gateway warehouse
    path('show-warehouses/', apiGatewayView.show_warehouses, name='List all created ubications'),
    path('create-warehouse/', apiGatewayView.create_warehouse, name='Create a new ubication'),
    path('update-warehouse/<int:pk>/', apiGatewayView.update_warehouse, name='Update a selected warehouse'),
    path('partial-update-warehouse/<int:pk>/', apiGatewayView.partial_update_warehouse, name='Update a selected attribute for a warehouse'),
    path('delete-warehouse/<int:pk>/', apiGatewayView.delete_warehouse, name='Delete a selected warehouse'),
    path('show-warehouse-buildings/<int:pk>/', apiGatewayView.show_warehouse_buildings, name='List all buildings by warehouse'),

    # API Gateway location
    path('show-locations/', apiGatewayView.show_locations, name='List all created locationns'),
    path('create-location/', apiGatewayView.create_location, name='Create a new location'),
    path('update-location/<int:pk>/', apiGatewayView.update_location, name='Update a selected location'),
    path('partial-update-location/<int:pk>/', apiGatewayView.partial_update_location, name='Update a selected attribute for a location'),
    path('delete-location/<int:pk>/', apiGatewayView.delete_location, name='Delete a selected location'),

    # API Gateway building
    path('show-buildings/', apiGatewayView.show_buildings, name='List all created buildings'),
    path('create-building/', apiGatewayView.create_building, name='Create a new building'),
    path('update-building/<int:pk>/', apiGatewayView.update_building, name='Update a selected building'),
    path('partial-update-building/<int:pk>/', apiGatewayView.partial_update_building, name='Update a selected attribute for a building'),
    path('delete-building/<int:pk>/', apiGatewayView.delete_building, name='Delete a selected building'),

    # API Gateway footprint
    path('show-footprints/', apiGatewayView.show_footprints, name='List all created footprints'),
    path('create-footprint/', apiGatewayView.create_footprint, name='Create a new footprint'),
    path('update-footprint/<int:pk>/', apiGatewayView.update_footprint, name='Update a selected footprint'),
    path('partial-update-footprint/<int:pk>/', apiGatewayView.partial_update_footprint, name='Update a selected attribute for a footprint'),
    path('delete-footprint/<int:pk>/', apiGatewayView.delete_footprint, name='Delete a selected footprint'),

    # API Gateway discount
    path('show-discounts/', apiGatewayView.show_discounts, name='List all created discounts'),
    path('create-discount/', apiGatewayView.create_discount, name='Create a new discount'),
    path('update-discount/<int:pk>/', apiGatewayView.update_discount, name='Update a selected discount'),
    path('partial-update-discount/<int:pk>/', apiGatewayView.partial_update_discount, name='Update a selected attribute for a discount'),
    path('delete-discount/<int:pk>/', apiGatewayView.delete_discount, name='Delete a selected discount'),

    # API Gateway price
    path('show-prices/', apiGatewayView.show_prices, name='List all created prices'),
    path('create-price/', apiGatewayView.create_price, name='Create a new price'),
    path('update-price/<int:pk>/', apiGatewayView.update_price, name='Update a selected price'),
    path('partial-update-price/<int:pk>/', apiGatewayView.partial_update_price, name='Update a selected attribute for a price'),
    path('delete-price/<int:pk>/', apiGatewayView.delete_price, name='Delete a selected price'),

    # API Gateway tax
    path('show-taxes/', apiGatewayView.show_taxes, name='List all created taxes'),
    path('create-tax/', apiGatewayView.create_tax, name='Create a new tax'),
    path('update-tax/<int:pk>/', apiGatewayView.update_tax, name='Update a selected tax'),
    path('partial-update-tax/<int:pk>/', apiGatewayView.partial_update_tax, name='Update a selected attribute for a tax'),
    path('delete-tax/<int:pk>/', apiGatewayView.delete_tax, name='Delete a selected tax'),

    # API Gateway product
    path('show-products/', apiGatewayView.show_products, name='List all created products'),
    path('create-product/', apiGatewayView.create_product, name='Create a new product'),
    path('update-product/<int:pk>/', apiGatewayView.update_product, name='Update a selected product'),
    path('partial-update-product/<int:pk>/', apiGatewayView.partial_update_product, name='Update a selected attribute for a product'),
    path('delete-product/<int:pk>/', apiGatewayView.delete_product, name='Delete a selected product'),
    path('show-product-discounts/<int:pk>/', apiGatewayView.show_product_discounts, name='List all discounts per product'),
    path('show-product-footprint/<int:pk>/', apiGatewayView.show_product_footprint, name='List footprint per products'),
    path('show-product-prices/<int:pk>/', apiGatewayView.show_product_prices, name='List all prices per products'),
    path('show-product-taxes/<int:pk>/', apiGatewayView.show_product_taxes, name='List all taxes per products'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# http://localhost:8000/swagger/
