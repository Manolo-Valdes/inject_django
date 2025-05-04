import inject


class DependencyManager:
    _bindings = {}
    _providers = {}

    @classmethod
    def add_singleton(cls, key, value):
        print('registering:', key)
        cls._bindings[key] = value

    @classmethod
    def add_provider(cls, key, value):
        print('registering:', key)
        cls._providers[key] = value

    @classmethod
    def config(cls, binder):
        [binder.bind(k, v) for k, v in cls._bindings.items()]
        [binder.bind_to_provider(k, v) for k, v in cls._providers.items()]

    @classmethod
    def configure(cls):
        print('configuring injector..')
        inject.configure(cls.config)
