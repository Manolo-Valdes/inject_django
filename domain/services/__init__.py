from domain.contracts.Basic import ILogger
from domain.services.basic import LoggerService
from domain.services.di import DependencyManager


def register_domain_services():
    print("Registering domain services..")
    DependencyManager.add_singleton(ILogger, LoggerService())
