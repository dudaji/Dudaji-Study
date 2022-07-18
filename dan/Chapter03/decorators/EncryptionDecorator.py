from decorators.DataSourceDecorator import DataSourceDecorator
import base64

class EncryptionDecorator(DataSourceDecorator):
    def writeData(self, data:str) -> None:
        super().writeData(self.__encode(data))

    def readData(self) -> str:
        return self.__decode(super().readData())

    def __encode(self, data:str) -> str:
        b64encoded = data.encode("utf-8")
        return base64.b64encode(b64encoded)

    def __decode(self, data) -> str:
        return data.decode("utf-8")
