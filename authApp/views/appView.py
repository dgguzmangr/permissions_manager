from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from authApp.models.user import User
from authApp.models.role import Role
from authApp.models.permission import Permission
from authApp.models.backupEmail import BackupEmail
from authApp.models.phone import Phone

from authApp.serializers.userSerializer import UserSerializer
from authApp.serializers.roleSerializer import RoleSerializer
from authApp.serializers.permissionSerializer import PermissionSerializer
from authApp.serializers.backupEmailSerializer import BackupEmailSerializer
from authApp.serializers.phoneSerializer import PhoneSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad

# User API

@swagger_auto_schema(method='get', responses={200: UserSerializer(many=True)} , tags=['User'])
@api_view(['GET'])
def show_users(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=UserSerializer, responses={201: UserSerializer}, tags=['User'])
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=UserSerializer, responses={200: UserSerializer}, tags=['User'])
@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=UserSerializer, responses={200: UserSerializer}, tags=['User'])
@api_view(['PATCH'])
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
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Role API

@swagger_auto_schema(method='get', responses={200: RoleSerializer(many=True)} , tags=['Role'])
@api_view(['GET'])
def show_roles(request):
    if request.method == 'GET':
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=RoleSerializer, responses={201: RoleSerializer}, tags=['Role'])
@api_view(['POST'])
def create_role(request):
    if request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=RoleSerializer, responses={200: RoleSerializer}, tags=['Role'])
@api_view(['PUT'])
def update_role(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except role.DoesNotExist:
        return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=RoleSerializer, responses={200: RoleSerializer}, tags=['Role'])
@api_view(['PATCH'])
def partial_update_role(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = RoleSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Role'])
@api_view(['DELETE'])
def delete_role(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Permission API

@swagger_auto_schema(method='get', responses={200: PermissionSerializer(many=True)} , tags=['Permission'])
@api_view(['GET'])
def show_permissions(request):
    if request.method == 'GET':
        permission = Permission.objects.all()
        serializer = PermissionSerializer(permission, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=PermissionSerializer, responses={201: PermissionSerializer}, tags=['Permission'])
@api_view(['POST'])
def create_permission(request):
    if request.method == 'POST':
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=PermissionSerializer, responses={200: PermissionSerializer}, tags=['Permission'])
@api_view(['PUT'])
def update_permission(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except permission.DoesNotExist:
        return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=PermissionSerializer, responses={200: PermissionSerializer}, tags=['Permission'])
@api_view(['PATCH'])
def partial_update_permission(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = PermissionSerializer(permission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Permission'])
@api_view(['DELETE'])
def delete_permission(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except Permission.DoesNotExist:
        return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# BackupEmail API

@swagger_auto_schema(method='get', responses={200: BackupEmailSerializer(many=True)} , tags=['BackupEmail'])
@api_view(['GET'])
def show_backupEmail(request):
    if request.method == 'GET':
        backupEmail = BackupEmail.objects.all()
        serializer = BackupEmailSerializer(backupEmail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=BackupEmailSerializer, responses={201: BackupEmailSerializer}, tags=['BackupEmail'])
@api_view(['POST'])
def create_backupEmail(request):
    if request.method == 'POST':
        serializer = BackupEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=BackupEmailSerializer, responses={200: BackupEmailSerializer}, tags=['BackupEmail'])
@api_view(['PUT'])
def update_backupEmail(request, pk):
    try:
        backupEmail = BackupEmail.objects.get(pk=pk)
    except backupEmail.DoesNotExist:
        return Response({"error": "Backup email not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BackupEmailSerializer(BackupEmail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=BackupEmailSerializer, responses={200: BackupEmailSerializer}, tags=['BackupEmail'])
@api_view(['PATCH'])
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
def show_phone(request):
    if request.method == 'GET':
        phone = Phone.objects.all()
        serializer = PhoneSerializer(Phone, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=PhoneSerializer, responses={201: PhoneSerializer}, tags=['Phone'])
@api_view(['POST'])
def create_phone(request):
    if request.method == 'POST':
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=PhoneSerializer, responses={200: PhoneSerializer}, tags=['Phone'])
@api_view(['PUT'])
def update_phone(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PhoneSerializer(Phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=PhoneSerializer, responses={200: PhoneSerializer}, tags=['Phone'])
@api_view(['PATCH'])
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
def delete_phone(request, pk):
    try:
        phone = Phone.objects.get(pk=pk)
    except Phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        phone.delete()
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