from threading import Lock, Thread

class Singleton(type):
    _instance = None
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SingletonClass(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

def run(value):
    singleton = SingletonClass(value)
    print(singleton.name)

if __name__ == '__main__':
    processa = Thread(target=run, args=('ACLASS',))
    processb = Thread(target=run, args=('BCLASS',))
    processa.start()
    processb.start()
    