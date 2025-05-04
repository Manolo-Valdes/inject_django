import inject


class DependencyManager:
    _dependencies = {}

    @classmethod
    def register(cls, key, value):
        print('registering:', key)
        cls._dependencies[key] = value

    @classmethod
    def do_binding(cls, binder):
        [binder.bind(k, v) for k, v in cls._dependencies.items()]

    @classmethod
    def configure(cls):
        print('configure:', cls._dependencies)
        inject.configure(cls.do_binding)
