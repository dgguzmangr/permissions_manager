from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authApp.models.role import Role
from authApp.models.permission import Permission

from authApp.serializers.roleSerializer import RoleSerializer
from authApp.serializers.permissionSerializer import PermissionSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad


# Role API

@api_view(['GET'])
def show_roles(request):
    if request.method == 'GET':
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_role(request):
    if request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET'])
def show_permissions(request):
    if request.method == 'GET':
        permission = Permission.objects.all()
        serializer = PermissionSerializer(permission, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_permission(request):
    if request.method == 'POST':
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['DELETE'])
def delete_permission(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except Permission.DoesNotExist:
        return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Login API

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)