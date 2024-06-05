from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.decorators import permission_required
from rest_framework.response import Response
from rest_framework import status
from authApp.serializers import UserSerializer, PermissionSerializer, BackupEmailSerializer, PhoneSerializer, UbicationSerializer, GroupSerializer
from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='get', responses={200: openapi.Response('Field structure', openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user': openapi.Schema(type=openapi.TYPE_OBJECT),
        'permission': openapi.Schema(type=openapi.TYPE_OBJECT),
        'backupEmail': openapi.Schema(type=openapi.TYPE_OBJECT),
        'phone': openapi.Schema(type=openapi.TYPE_OBJECT),
        'ubication': openapi.Schema(type=openapi.TYPE_OBJECT),
        'group': openapi.Schema(type=openapi.TYPE_OBJECT),
    }
))}, tags=['Field structure view'])
@api_view(['GET'])
@permission_classes([])  # Ajustar según sea necesario
@authentication_classes([])  # Ajustar según sea necesario
def permissions_field_structure_view(request):
    userSerializer = UserSerializer()
    permissionSerializer = PermissionSerializer()
    backupEmailSerializer = BackupEmailSerializer()
    phoneSerializer = PhoneSerializer()
    ubicationSerializer = UbicationSerializer()
    groupSerializer = GroupSerializer()

    user_fields = get_serializer_fields_info(userSerializer)
    permission_fields = get_serializer_fields_info(permissionSerializer)
    backupEmail_fields = get_serializer_fields_info(backupEmailSerializer)
    phone_fields = get_serializer_fields_info(phoneSerializer)
    ubication_fields = get_serializer_fields_info(ubicationSerializer)
    group_fields = get_serializer_fields_info(groupSerializer)

    field_structure = {
        'user': user_fields,
        'permission': permission_fields,
        'backupEmail': backupEmail_fields,
        'phone': phone_fields,
        'ubication': ubication_fields,
        'group': group_fields,
    }

    return Response(field_structure, status=status.HTTP_200_OK)


def get_serializer_fields_info(serializer):
    fields_info = {}

    for field_name, field in serializer.fields.items():
        field_info = {
            'required': field.required,
            'read_only': field.read_only,
            'validations': get_field_validations(field),
            'choices': None
        }

        # Obtener las choices si existen
        if hasattr(field, 'choices'):
            field_info['choices'] = dict(field.choices)

        fields_info[field_name] = field_info

    return fields_info


def get_field_validations(field):
    validations = []

    max_length = getattr(field, 'max_length', None)
    if max_length is not None:
        validations.append(f"Max length: {max_length}")

    max_value = getattr(field, 'max_value', None)
    if max_value is not None:
        validations.append(f"Max value: {max_value}")

    min_value = getattr(field, 'min_value', None)
    if min_value is not None:
        validations.append(f"Min value: {min_value}")

    validators = getattr(field, 'validators', None)
    if validators:
        for validator in validators:
            validations.append(str(validator))

    return validations
