from domain.contracts.Basic import ILogger


class LoggerService(ILogger):

    def log_information(self, msg: str):
        print(msg)
