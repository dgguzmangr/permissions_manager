from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad


def standard_response(success, message, data=None, status_code=status.HTTP_200_OK):
    response = {
        'success': success,
        'message': message,
        'data': data
    }
    return Response(response, status=status_code)


class UserController:


    @staticmethod
    @api_view(['GET'])
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def show_users(request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return standard_response(True, "Users retrieved successfully", serializer.data)
        except Exception as e:
            return standard_response(False, str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @staticmethod
    @api_view(['POST'])
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def create_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return standard_response(True, "User created successfully", serializer.data, status.HTTP_201_CREATED)
        return standard_response(False, "User creation failed", serializer.errors, status.HTTP_400_BAD_REQUEST)


    @staticmethod
    @api_view(['PUT'])
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def update_user(request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return standard_response(False, "User not found", status_code=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return standard_response(True, "User updated successfully", serializer.data)
        return standard_response(False, "User update failed", serializer.errors, status.HTTP_400_BAD_REQUEST)


    @staticmethod
    @api_view(['DELETE'])
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def delete_user(request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return standard_response(False, "User not found", status_code=status.HTTP_404_NOT_FOUND)

        user.delete()
        return standard_response(True, "User deleted successfully", data=None, status_code=status.HTTP_204_NO_CONTENT)


    @api_view(['POST'])
    def login(request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return standard_response(False, "Email and password are required", status_code=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return standard_response(True, "Login successful", {'token': token.key})
        else:
            return standard_response(False, "Invalid credentials", status_code=status.HTTP_401_UNAUTHORIZED)


