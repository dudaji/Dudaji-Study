import base64
from DataSourceDecorator import DataSourceDecorator
from DataSource import DataSource

class EncryptionDecorator(DataSourceDecorator):

    def __init__(self, wrappee: DataSource):
        super().__init__(wrappee)

    def writeData(self, data: bytes) -> None:
        b64data = base64.b64encode(data)
        # self.wrappee.writeData(b64data)
        super().writeData(b64data)

    def readData(self) -> bytes:
        data = super().readData()
        b64data = base64.b64decode(data)
        return b64data
