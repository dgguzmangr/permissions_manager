from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad


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