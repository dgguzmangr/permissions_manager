from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authApp.serializers import PermissionSerializer, RoleSerializer, RolePermissionSerializer, UserRoleSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad


@api_view(['GET'])
def field_structure_view(request):
    permissionSerializer = PermissionSerializer()
    roleSerializer = RoleSerializer()
    rolePermissionSerializer = RolePermissionSerializer()
    userRoleSerializer = UserRoleSerializer()

    permission_fields = get_serializer_fields_info(permissionSerializer)
    role_fields = get_serializer_fields_info(roleSerializer)
    rolePermission_fields = get_serializer_fields_info(rolePermissionSerializer)
    userRole_fields = get_serializer_fields_info(userRoleSerializer)

    field_structure = {
        'permission': permission_fields,
        'role': role_fields,
        'rolePermission': rolePermission_fields,
        'userRole': userRole_fields
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
