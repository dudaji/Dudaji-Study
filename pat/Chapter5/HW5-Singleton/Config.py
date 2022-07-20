from Singleton import Singleton

class Config(metaclass=Singleton):

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location
