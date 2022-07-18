from decorators.DataSourceDecorator import DataSourceDecorator
import zlib

class CompressionDecorator(DataSourceDecorator):
    __compLevel = 0
    def getCompressionLevel(self) -> int:
        return self.__compLevel

    def setCompressionLevel(self, value:int) -> None:
        self.__compLevel = value

    def writeData(self, data:str) -> None:
        return super().writeData(self.__compress(data))

    def readData(self) -> str:
        return self.__decompress(super().readData())

    def __compress(self, stringData:str):
        return str(zlib.compress(bytearray(stringData, encoding="utf-8"), self.__compLevel))

    def __decompress(self, stringData:str):
        return str(zlib.decompress(stringData))
    