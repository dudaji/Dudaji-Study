import abc

class DataSource(abc.ABC):
    @abc.abstractmethod
    def writeData(self, data):
        pass

    @abc.abstractmethod
    def readData(self):
        pass
