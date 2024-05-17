from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad
