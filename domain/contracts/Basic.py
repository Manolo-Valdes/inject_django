from abc import ABC, abstractmethod


class IGreetings(ABC):
    @abstractmethod
    def hello(self, user: str) -> str:
        pass


class ILogger(ABC):
    @abstractmethod
    def log_information(self, msg: str):
        pass
