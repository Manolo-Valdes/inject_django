from abc import ABC, abstractmethod


class IGreetings(ABC):
    @abstractmethod
    def hello(self, user: str) -> str:
        pass

