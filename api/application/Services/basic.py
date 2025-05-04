import inject

from domain.contracts.Basic import IGreetings, ILogger


class GreetingsService(IGreetings):

    @inject.autoparams
    def __init__(self, logger: ILogger):
        super().__init__()
        self.logger = logger

    def hello(self, user: str) -> str:
        self.logger.log_information('Hello {}'.format(user))
        return f"Hello {user}"
