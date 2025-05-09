from django.core.management.base import BaseCommand
from drf_yasg import openapi
import json
import yaml
from exam_app.urls import schema_view


class Command(BaseCommand):
    help = 'Generate Swagger documentation files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--format',
            choices=['json', 'yaml'],
            default='json',
            help='Output format (json or yaml)',
        )
        parser.add_argument(
            '--output', type=str, required=True, help='Output file path'
        )

    def handle(self, *args, **options):
        from rest_framework.test import APIRequestFactory
        from django.test.utils import override_settings

        with override_settings(ALLOWED_HOSTS=['testserver', 'localhost', '127.0.0.1']):
            factory = APIRequestFactory()
            request = factory.get('/swagger.json', HTTP_HOST='localhost')

            response = schema_view.without_ui(cache_timeout=0)(request, format='.json')
            schema = response.data

        output_file = options['output']
        output_format = options['format']

        with open(output_file, 'w') as f:
            if output_format == 'json':
                content = json.dumps(schema, indent=2)
            else:
                content = yaml.dump(schema)
            f.write(content)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully generated {output_format} documentation to {output_file}'
            )
        )
