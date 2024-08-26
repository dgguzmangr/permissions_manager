# Generated by Django 4.1.13 on 2024-08-26 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0009_alter_user_company_name_alter_user_document_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('authApp.show_users', 'Can view users'), ('authApp.create_users', 'Can create users'), ('authApp.update_users', 'Can update users'), ('authApp.partial_update_users', 'Can update partially users'), ('authApp.delete_users', 'Can delete users'), ('authApp.show_warehouses', 'Can view warehouses'), ('authApp.create_warehouses', 'Can create warehouses'), ('authApp.update_warehouses', 'Can update warehouses'), ('authApp.partial_update_warehouses', 'Can update partially warehouses'), ('authApp.delete_warehouses', 'Can delete warehouses'), ('authApp.show_warehouse_buildings', 'Can view buildings filtered by warehouses'), ('authApp.show_locations', 'Can view locations'), ('authApp.create_locations', 'Can create locations'), ('authApp.update_locations', 'Can update locations'), ('authApp.partial_update_locations', 'Can update partially locations'), ('authApp.delete_locations', 'Can delete locations'), ('authApp.show_buildings', 'Can view buildings'), ('authApp.create_buildings', 'Can create buildings'), ('authApp.update_buildings', 'Can update buildings'), ('authApp.partial_update_buildings', 'Can update partially buildings'), ('authApp.delete_buildings', 'Can delete buildings'), ('authApp.show_footprints', 'Can view footprints'), ('authApp.create_footprints', 'Can create footprints'), ('authApp.update_footprints', 'Can update footprints'), ('authApp.partial_update_footprints', 'Can update partially footprints'), ('authApp.delete_footprints', 'Can delete footprints'), ('authApp.show_discounts', 'Can view discounts'), ('authApp.create_discounts', 'Can create discounts'), ('authApp.update_discounts', 'Can update discounts'), ('authApp.partial_update_discounts', 'Can update partially discounts'), ('authApp.delete_discounts', 'Can delete discounts'), ('authApp.show_prices', 'Can view prices'), ('authApp.create_prices', 'Can create prices'), ('authApp.update_prices', 'Can update prices'), ('authApp.partial_update_prices', 'Can update partially prices'), ('authApp.delete_prices', 'Can delete prices'), ('authApp.show_taxes', 'Can view taxes'), ('authApp.create_taxes', 'Can create taxes'), ('authApp.update_taxes', 'Can update taxes'), ('authApp.partial_update_taxes', 'Can update partially taxes'), ('authApp.delete_taxes', 'Can delete taxes'), ('authApp.show_products', 'Can view products'), ('authApp.create_products', 'Can create products'), ('authApp.update_products', 'Can update products'), ('authApp.partial_update_products', 'Can update partially products'), ('authApp.delete_products', 'Can delete products'), ('authApp.show_product_discounts', 'Can view discounts filtered by products'), ('authApp.show_product_footprints', 'Can view footprints filtered by products'), ('authApp.show_product_prices', 'Can view prices filtered by products'), ('authApp.show_product_taxes', 'Can view taxes filtered by products'), ('authApp.show_product_details', 'Get product details'), ('authApp.products_field_structure_view', 'Gets the field structure of the products backend'), ('authApp.warehouse_field_structure_view', 'Gets the field structure of the warehouse backend')]},
        ),
    ]
