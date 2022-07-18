from threading import Lock

from observer.observer import ObserverManager


class SingletonMeta(type):
    _instances: dict = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SafeSingleton(metaclass=SingletonMeta):
    def __init__(self, value=None):
        self.value = value
        self.manager: ObserverManager = ObserverManager()

    def set_value(self, value):
        self.value = value

    @classmethod
    def delete_instance(cls):
        if cls in cls._instances:
            with cls._lock:
                if cls in cls._instances:
                    del cls._instances[cls]

    def subscribe(self, observer):
        self.manager.register(observer)

    def unsubscribe(self, observer):
        self.manager.remove(observer)

    def update_value(self, value):
        self.set_value(value)
        self.manager.update_value(self.value)
