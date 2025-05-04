from domain.contracts.Basic import IGreetings


class GreetingsService(IGreetings):
    def hello(self, user: str) -> str:
        return f"Hello {user}"


