from django.apps import AppConfig

from api.application.injector_config import register_services


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        register_services()