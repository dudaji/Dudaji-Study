import random

class NotThreadSafe(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

class SingleThread(NotThreadSafe):
    __value = None
    def __init__(self):
        self.__value = random.randrange(1, 99999)
        
    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
    