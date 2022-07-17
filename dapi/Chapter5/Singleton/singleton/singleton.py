from threading import Lock

lock = Lock()

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SafeSingleton(metaclass=Singleton):
    value: str = None

    def __init__(self, value=None):
        self.value = value

    def set_value(self, value):
        self.value = value

    @classmethod
    def delete_instance(cls):
        if cls in cls._instances:
            with lock:
                if cls in cls._instances:
                    del cls._instances[cls]
