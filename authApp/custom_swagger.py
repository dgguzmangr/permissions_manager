from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.generators import OpenAPISchemaGenerator

class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = super().get_tags(operation_keys)
        return sorted(tags)

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        # Verificar si schema.tags existe antes de ordenarlo
        if hasattr(schema, 'tags') and schema.tags:
            schema.tags = sorted(schema.tags, key=lambda tag: tag['name'])
        return schema
