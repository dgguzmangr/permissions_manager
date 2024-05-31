from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import requests
from decouple import config
from django.conf import settings


from rest_framework.authtoken.models import Token  # comentar para deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm  # comentar para deshabilitar seguridad
from django.contrib.auth import login as auth_login  # comentar para deshabilitar seguridad

response_200 = openapi.Response(description="Successful response")
response_400 = openapi.Response(description="Bad request")
response_500 = openapi.Response(description="Internal server error")

# Warehouse API

warehouse_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the warehouse'),
        'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
        'department': openapi.Schema(type=openapi.TYPE_STRING, description='Department'),
        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City'),
        'neighborthood': openapi.Schema(type=openapi.TYPE_STRING, description='Neighborhood'),
        'address': openapi.Schema(type=openapi.TYPE_STRING, description='Address'),
        'postal_code': openapi.Schema(type=openapi.TYPE_STRING, description='Postal Code'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location (Geo Point)'),
        'building': openapi.Schema(type=openapi.TYPE_INTEGER, description='Building ID'),
    },
    required=['name', 'country', 'department', 'city', 'neighborthood', 'address', 'postal_code', 'location', 'building']
)

@swagger_auto_schema(method='get', tags=['Warehouse'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def show_warehouses(request):
    try:
        url = f"{config('url_warehouse_manager')}/show-warehouses/"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Error getting warehouses"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='post', request_body=warehouse_schema, responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'}, tags=['Warehouse'])
@api_view(['POST'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def create_warehouse(request):
    try:
        url = f"{config('url_warehouse_manager')}/create-warehouse/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Error creating warehouses"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='put', request_body=warehouse_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Warehouse'])
@api_view(['PUT'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def update_warehouse(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/update-warehouse/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error updating warehouse"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='patch', request_body=warehouse_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Warehouse'])
@api_view(['PATCH'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def partial_update_warehouse(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/partial-update-warehouse/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error partially updating warehouse"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='delete', responses={204: 'No Content', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Warehouse'])
@api_view(['DELETE'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def delete_warehouse(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/delete-warehouse/{pk}/"
        response = requests.delete(url)
        
        if response.status_code == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error deleting warehouse"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='get', tags=['Warehouse'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def show_warehouse_buildings(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/show-warehouse-buildings/{pk}/"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Error getting buildings from warehouse"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Location API

location_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'location_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the location', readOnly=True),
        'type': openapi.Schema(type=openapi.TYPE_STRING, description='Type of the location'),
        'long': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Length of the location'),
        'high': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Height of the location'),
        'width': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Width of the location'),
        'weight': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Weight capacity of the location'),
        'volume': openapi.Schema(type=openapi.TYPE_NUMBER, format='float', description='Volume of the location', readOnly=True),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the location')
    },
    required=['type', 'long', 'high', 'width', 'weight', 'description']
)

@swagger_auto_schema(method='get', tags=['Location'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def show_locations(request):
    try:
        url = f"{config('url_warehouse_manager')}/show-locations/"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Error getting locations"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='post', request_body=location_schema, responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'}, tags=['Location'])
@api_view(['POST'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def create_location(request):
    try:
        url = f"{config('url_warehouse_manager')}/create-location/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Error creating location"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='put', request_body=location_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Location'])
@api_view(['PUT'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def update_location(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/update-location/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error updating location"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='patch', request_body=location_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Location'])
@api_view(['PATCH'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def partial_update_location(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/partial-update-location/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error partially updating location"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='delete', responses={204: 'No Content', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Location'])
@api_view(['DELETE'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def delete_location(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/delete-location/{pk}/"
        response = requests.delete(url)
        
        if response.status_code == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error deleting location"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Building API
building_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'building_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the building', readOnly=True),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the building'),
        'location': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the location associated with the building')
    },
    required=['name', 'location']
)

@swagger_auto_schema(method='get', tags=['Building'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def show_buildings(request):
    try:
        url = f"{config('url_warehouse_manager')}/show-buildings/"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Error getting locations"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='post', request_body=building_schema, responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'}, tags=['Building'])
@api_view(['POST'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def create_building(request):
    try:
        url = f"{config('url_warehouse_manager')}/create-building/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Error creating building"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='put', request_body=building_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Building'])
@api_view(['PUT'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def update_building(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/update-building/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error updating building"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='patch', request_body=building_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Building'])
@api_view(['PATCH'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def partial_update_building(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/partial-update-building/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error partially updating building"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='delete', responses={204: 'No Content', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Building'])
@api_view(['DELETE'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def delete_building(request, pk):
    try:
        url = f"{config('url_warehouse_manager')}/delete-building/{pk}/"
        response = requests.delete(url)
        
        if response.status_code == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error deleting building"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Footprint API
footprint_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'footprint_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the footprint', readOnly=True),
        'measurement_unit': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Measurement unit of the footprint',
            enum=[
                'Gramo', 'Kilogramo', 'Tonelada', 'Mililitro', 'Litro', 'Metro cúbico', 'Metro', 'Centímetro',
                'Metro cuadrado', 'Palet', 'Caja', 'Paquete', 'Botella', 'Barril', 'Contenedor'
            ]
        ),
        'long': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Length of the footprint'),
        'high': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Height of the footprint'),
        'width': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Width of the footprint'),
        'weight': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Weight of the footprint'),
        'volume': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Volume of the footprint', readOnly=True),
    },
    required=['measurement_unit', 'long', 'high', 'width', 'weight']
)

@swagger_auto_schema(method='get', tags=['Footprint'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def show_footprints(request):
    try:
        url = f"{config('url_product_manager')}/show-footprints/"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Error getting footprints"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='post', request_body=footprint_schema, responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'}, tags=['Footprint'])
@api_view(['POST'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def create_footprint(request):
    try:
        url = f"{config('url_product_manager')}/create-footprint/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Error creating footprint"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='put', request_body=footprint_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Footprint'])
@api_view(['PUT'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def update_footprint(request, pk):
    try:
        url = f"{config('url_product_manager')}/update-footprint/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error updating footprint"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='patch', request_body=footprint_schema, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Footprint'])
@api_view(['PATCH'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def partial_update_footprint(request, pk):
    try:
        url = f"{config('url_product_manager')}/partial-update-footprint/{pk}/"
        payload = request.data
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error partially updating footprint"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='delete', responses={204: 'No Content', 404: 'Not Found', 500: 'Internal Server Error'}, tags=['Footprint'])
@api_view(['DELETE'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def delete_footprint(request, pk):
    try:
        url = f"{config('url_product_manager')}/delete-footprint/{pk}/"
        response = requests.delete(url)
        
        if response.status_code == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif response.status_code == 404:
            return Response(response.json(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Error deleting footprint"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Discount API
discount_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'discount_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the discount', readOnly=True),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date when the discount was created', readOnly=True),
        'amount': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Discount amount in percentage'),
        'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Status of the discount')
    },
    required=['amount', 'status']
)






















# Price API
price_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'price_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the price', readOnly=True),
        'amount': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal', description='Monetary amount'),
                'currency': openapi.Schema(type=openapi.TYPE_STRING, description='Currency code')
            },
            required=['amount', 'currency'],
            description='Amount with currency'
        ),
        'date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date of the price', readOnly=True),
        'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Status of the price')
    },
    required=['amount', 'status']
)

# Tax API
tax_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'tax_id': openapi.Schema(
            type=openapi.TYPE_INTEGER, 
            description='ID of the tax', 
            readOnly=True
        ),
        'name': openapi.Schema(
            type=openapi.TYPE_STRING, 
            description='Name of the tax',
            maxLength=100
        ),
        'percentage': openapi.Schema(
            type=openapi.TYPE_NUMBER, 
            format='decimal', 
            description='Percentage of the tax',
            maximum=100,
            minimum=0,
        ),
        'status': openapi.Schema(
            type=openapi.TYPE_BOOLEAN, 
            description='Status of the tax'
        ),
    },
    required=['name', 'percentage', 'status']
)

# Product API
product_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'product_id': openapi.Schema(
            type=openapi.TYPE_INTEGER, 
            description='ID of the product', 
            readOnly=True
        ),
        'sku': openapi.Schema(
            type=openapi.TYPE_STRING, 
            description='SKU of the product', 
            readOnly=True
        ),
        'name': openapi.Schema(
            type=openapi.TYPE_STRING, 
            description='Name of the product', 
            maxLength=100
        ),
        'short_description': openapi.Schema(
            type=openapi.TYPE_STRING, 
            description='Short description of the product', 
            maxLength=30
        ),
        'long_description': openapi.Schema(
            type=openapi.TYPE_STRING, 
            description='Long description of the product', 
            maxLength=100
        ),
        'footprint': openapi.Schema(
            type=openapi.TYPE_INTEGER, 
            description='ID of the associated footprint'
        ),
        'price': openapi.Schema(
            type=openapi.TYPE_INTEGER, 
            description='ID of the associated price'
        ),
        'discount': openapi.Schema(
            type=openapi.TYPE_INTEGER, 
            description='ID of the associated discount'
        ),
        'tax': openapi.Schema(
            type=openapi.TYPE_INTEGER, 
            description='ID of the associated tax'
        )
    },
    required=['name', 'short_description', 'long_description', 'footprint', 'price', 'discount', 'tax']
)
