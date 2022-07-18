from decorators.DataSource import DataSource

class DataSourceDecorator(DataSource):
    def __init__(self, source) -> None:
        self.__wrappee = source

    def writeData(self, data) -> None:
        self.__wrappee.writeData(data)

    def readData(self) -> str:
        return self.__wrappee.readData()
    