from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authApp.models.role import Role
from authApp.models.permission import Permission
from authApp.models.userRole import UserRole
from authApp.models.rolePermission import RolePermission

from authApp.serializers.roleSerializer import RoleSerializer
from authApp.serializers.permissionSerializer import PermissionSerializer
from authApp.serializers.userRoleSerializer import UserRoleSerializer
from authApp.serializers.rolePermissionSerializer import RolePermissionSerializer

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

# UserRole API

@api_view(['GET'])
def show_user_roles(request):
    if request.method == 'GET':
        userRole = UserRole.objects.all()
        serializer = UserRoleSerializer(userRole, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user_rol(request):
    if request.method == 'POST':
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user_rol(request, pk):
    try:
        userRole = UserRole.objects.get(pk=pk)
    except userRole.DoesNotExist:
        return Response({"error": "User rol not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserRoleSerializer(userRole, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user_rol(request, pk):
    try:
        userRole = UserRole.objects.get(pk=pk)
    except UserRole.DoesNotExist:
        return Response({"error": "User rol not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        userRole.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Rol and Permission API

@api_view(['GET', 'POST'])
def user_role_list(request):
    if request.method == 'GET':
        user_roles = UserRole.objects.all()
        serializer = UserRoleSerializer(user_roles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def role_permission_list(request):
    if request.method == 'GET':
        role_permissions = RolePermission.objects.all()
        serializer = RolePermissionSerializer(role_permissions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RolePermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def check_permission(request):
    user_id = request.GET.get('user_id')
    permission_name = request.GET.get('permission_name')
    
    if not user_id or not permission_name:
        return Response({'error': 'user_id and permission_name are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_roles = UserRole.objects.filter(user_id=user_id)
        if user_roles.exists():
            roles = user_roles.values_list('role', flat=True)
            if RolePermission.objects.filter(role__in=roles, permission__name=permission_name).exists():
                return Response({'permission': 'granted'}, status=status.HTTP_200_OK)
        return Response({'permission': 'denied'}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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