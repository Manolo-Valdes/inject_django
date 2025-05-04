from django.apps import AppConfig

from api.application.Services.basic import GreetingsService
from domain.contracts.Basic import IGreetings
from domain.services.di import DependencyManager


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        print("Registering api dependency injection")
        DependencyManager.add_provider(IGreetings, lambda: GreetingsService())
