import inject

from domain.contracts.Basic import IGreetings, ILogger


class GreetingsService(IGreetings):

    def __init__(self):
        super().__init__()
        print('GreetingsService initialized')
        self.logger = inject.instance(ILogger)

    def hello(self, user: str) -> str:
        self.logger.log_information('Hello {}'.format(user))
        return f"Hello {user}"
