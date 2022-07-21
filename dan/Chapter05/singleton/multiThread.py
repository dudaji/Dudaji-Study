import random
from threading import Lock

class Singleton(object):
    __instance = None
    __lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if not isinstance(cls.__instance, cls):
                cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

class MultiThread(Singleton):
    __value = None
    def __init__(self):
        self.__value = random.randrange(1, 99999)
        
    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
    