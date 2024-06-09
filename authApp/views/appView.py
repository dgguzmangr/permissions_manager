from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.decorators import permission_classes
from decouple import config, UndefinedValueError
from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from authApp.models.user import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from authApp.models.backupEmail import BackupEmail
from authApp.models.phone import Phone
from authApp.models.ubication import Ubication

from authApp.serializers.userSerializer import UserSerializer
from authApp.serializers.groupSerializer import GroupSerializer
from authApp.serializers.permissionSerializer import PermissionSerializer
from authApp.serializers.backupEmailSerializer import BackupEmailSerializer
from authApp.serializers.phoneSerializer import PhoneSerializer
from authApp.serializers.ubicationSerializer import UbicationSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad

# User API

@swagger_auto_schema(method='get', responses={200: UserSerializer(many=True)} , tags=['User'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def show_users(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""
@swagger_auto_schema(method='post', request_body=UserSerializer, responses={201: UserSerializer}, tags=['User'])
@api_view(['POST'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

@swagger_auto_schema(method='post', request_body=UserSerializer, responses={201: UserSerializer}, tags=['User'])
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def create_user(request):
    if request.method == 'POST':
        serializer = User(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            
            # Actualizar el user en el microservicio de usuarios
            product_id = user['product_id']
            user_id = user['id']
            product_update_url = f"{config('url_product_manager')}/show-products/"
            requests.post(product_update_url, json={'user_id': user_id})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










@swagger_auto_schema(method='put', request_body=UserSerializer, responses={200: UserSerializer}, tags=['User'])
@api_view(['PUT'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def update_user(request, pk):
    queryset = User.objects.all()  # Definir el queryset

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:  # Corrige el typo: user -> User
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=UserSerializer, responses={200: UserSerializer}, tags=['User'])
@api_view(['PATCH'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def partial_update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['User'])
@api_view(['DELETE'])
@permission_classes([])
@authentication_classes([])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Group API

@swagger_auto_schema(method='get', responses={200: GroupSerializer(many=True)}, tags=['Group'])
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def show_groups(request):
    queryset = Group.objects.all()
    if request.method == 'GET':
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=GroupSerializer, responses={201: GroupSerializer}, tags=['Group'])
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_group(request):
    if request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=GroupSerializer, responses={200: GroupSerializer}, tags=['Group'])
@api_view(['PUT'])
@permission_classes([])  # Ajustar según tus necesidades
@authentication_classes([])  # Ajustar según tus necesidades
def update_group(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except group.DoesNotExist:
        return Response({"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=GroupSerializer, responses={200: GroupSerializer}, tags=['Group'])
@api_view(['PATCH'])
@permission_classes([])
@authentication_classes([])
def partial_update_group(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response({"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Group'])
@api_view(['DELETE'])
@permission_classes([])
@authentication_classes([])
def delete_group(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response({"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Group ID'),
    }
), responses={201: 'Group assigned to user successfully', 400: 'Bad Request'}, tags=['Group'])
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def assign_group_to_user(request):
    user_id = request.data.get('user_id')
    id = request.data.get('id')
    try:
        user = User.objects.get(pk=user_id)
        group = Group.objects.get(pk=id)
        user.user_groups.add(group)  # Usar el campo correcto 'user_groups'
        return Response({'message': 'Group assigned to user successfully'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Group.DoesNotExist:
        return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Permission API

@swagger_auto_schema(method='get', responses={200: PermissionSerializer(many=True)}, tags=['Permission'])
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def show_permissions(request):
    queryset = Permission.objects.all()
    if request.method == 'GET':
        serializer = PermissionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Group ID'),
        'permission_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Permission ID'),
    }
), responses={201: 'Permission assigned to group successfully', 400: 'Bad Request'}, tags=['Permission'])
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def assign_permission_to_group(request):
    id = request.data.get('id')
    permission_id = request.data.get('permission_id')
    try:
        group = Group.objects.get(pk=id)
        permission = Permission.objects.get(pk=permission_id)
        group.permissions.add(permission)
        return Response({'message': 'Permission assigned to group successfully'}, status=status.HTTP_200_OK)
    except Group.DoesNotExist:
        return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
    except Permission.DoesNotExist:
        return Response({'error': 'Permission not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# BackupEmail API

@swagger_auto_schema(method='get', responses={200: BackupEmailSerializer(many=True)} , tags=['BackupEmail'])
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def show_backupEmail(request):
    if request.method == 'GET':
        backupEmail = BackupEmail.objects.all()
        serializer = BackupEmailSerializer(backupEmail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=BackupEmailSerializer, responses={201: BackupEmailSerializer}, tags=['BackupEmail'])
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_backupEmail(request):
    if request.method == 'POST':
        serializer = BackupEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=BackupEmailSerializer, responses={200: BackupEmailSerializer}, tags=['BackupEmail'])
@api_view(['PUT'])
@permission_classes([])
@authentication_classes([])
def update_backupEmail(request, pk):
    try:
        backupEmail = BackupEmail.objects.get(pk=pk)
    except backupEmail.DoesNotExist:
        return Response({"error": "Backup email not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BackupEmailSerializer(backupEmail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=BackupEmailSerializer, responses={200: BackupEmailSerializer}, tags=['BackupEmail'])
@api_view(['PATCH'])
@permission_classes([])
@authentication_classes([])
def partial_update_backupEmail(request, pk):
    try:
        backupEmail = BackupEmail.objects.get(pk=pk)
    except BackupEmail.DoesNotExist:
        return Response({"error": "Backup email not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = BackupEmailSerializer(backupEmail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['BackupEmail'])
@api_view(['DELETE'])
@permission_classes([])
@authentication_classes([])
def delete_backupEmail(request, pk):
    try:
        backupEmail = BackupEmail.objects.get(pk=pk)
    except BackupEmail.DoesNotExist:
        return Response({"error": "Backup email not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        backupEmail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Phone API

@swagger_auto_schema(method='get', responses={200: PhoneSerializer(many=True)} , tags=['Phone'])
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def show_phone(request):
    if request.method == 'GET':
        phone = Phone.objects.all()
        serializer = PhoneSerializer(phone, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=PhoneSerializer, responses={201: PhoneSerializer}, tags=['Phone'])
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_phone(request):
    if request.method == 'POST':
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=PhoneSerializer, responses={200: PhoneSerializer}, tags=['Phone'])
@api_view(['PUT'])
@permission_classes([])
@authentication_classes([])
def update_phone(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PhoneSerializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=PhoneSerializer, responses={200: PhoneSerializer}, tags=['Phone'])
@api_view(['PATCH'])
@permission_classes([])
@authentication_classes([])
def partial_update_phone(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except Phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = PhoneSerializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Phone'])
@api_view(['DELETE'])
@permission_classes([])
@authentication_classes([])
def delete_phone(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except Phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Ubication API

@swagger_auto_schema(method='get', responses={200: UbicationSerializer(many=True)} , tags=['Ubication'])
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def show_ubication(request):
    if request.method == 'GET':
        ubication = Ubication.objects.all()
        serializer = UbicationSerializer(ubication, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=UbicationSerializer, responses={201: UbicationSerializer}, tags=['Ubication'])
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def create_ubication(request):
    if request.method == 'POST':
        serializer = UbicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=UbicationSerializer, responses={200: UbicationSerializer}, tags=['Ubication'])
@api_view(['PUT'])
@permission_classes([])
@authentication_classes([])
def update_ubication(request, pk):
    try:
        ubication = Ubication.objects.get(pk=pk)
    except ubication.DoesNotExist:
        return Response({"error": "Ubication not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UbicationSerializer(ubication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=UbicationSerializer, responses={200: UbicationSerializer}, tags=['Ubication'])
@api_view(['PATCH'])
@permission_classes([])
@authentication_classes([])
def partial_update_ubication(request, pk):
    try:
        ubication = Ubication.objects.get(pk=pk)
    except Ubication.DoesNotExist:
        return Response({"error": "Ubication not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = UbicationSerializer(ubication, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Ubication'])
@api_view(['DELETE'])
@permission_classes([])
@authentication_classes([])
def delete_ubication(request, pk):
    try:
        ubication = Ubication.objects.get(pk=pk)
    except Ubication.DoesNotExist:
        return Response({"error": "Ubication not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        ubication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Login API

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user')
        }
    ),
    responses={
        200: openapi.Response(
            description="Successful login",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token')
                }
            )
        ),
        400: openapi.Response(
            description="Invalid username or password",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message')
                }
            )
        )
    },
    tags=['Authentication']
)
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)