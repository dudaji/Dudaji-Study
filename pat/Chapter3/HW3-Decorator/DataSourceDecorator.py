# from abc import abstractmethod
from DataSource import DataSource

class DataSourceDecorator(DataSource):

    def __init__(self, src: DataSource):
        self.wrappee = src

    def writeData(self, data: bytes) -> None:
        self.wrappee.writeData(data)

    def readData(self) -> bytes:
        return self.wrappee.readData()

