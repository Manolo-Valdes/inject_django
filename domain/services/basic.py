from domain.contracts.Basic import ILogger


class LoggerService(ILogger):
    def __init__(self):
        print('LoggerService initialized')

    def log_information(self, msg: str):
        print(msg)
