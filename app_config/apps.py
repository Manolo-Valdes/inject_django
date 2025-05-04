from django.apps import AppConfig

from domain.services.di import DependencyManager


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_config'

    def ready(self):
        print("Ready")
        DependencyManager.configure()
