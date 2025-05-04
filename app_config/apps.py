from django.apps import AppConfig

from domain.services import register_domain_services
from domain.services.di import DependencyManager


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_config'

    def ready(self):
        register_domain_services()
        DependencyManager.configure()
        print('app_config ready!')
