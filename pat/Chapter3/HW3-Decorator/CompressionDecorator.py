import zlib
from DataSourceDecorator import DataSourceDecorator
from DataSource import DataSource

class CompressionDecorator(DataSourceDecorator):
    
    def __init__(self, wrappee: DataSource):
        super().__init__(wrappee)

    def writeData(self, data: bytes) -> None:
        compdata = zlib.compress(data)
        # self.wrappee.writeData(compdata)
        super().writeData(compdata)

    def readData(self) -> bytes:
        compdata = super().readData()
        data = zlib.decompress(compdata)
        return data
