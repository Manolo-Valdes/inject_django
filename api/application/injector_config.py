from api.application.Services.basic import GreetingsService
from domain.contracts.Basic import IGreetings
from domain.services import DependencyManager


def register_services():
    print("Registering api dependency injection")
    DependencyManager.add_provider(IGreetings, lambda: GreetingsService())
