from DataSource import DataSource

class FileDataSource(DataSource):

    def __init__(self, filename: str):
        self.filename = filename

    def writeData(self, data: bytes) -> None:
        with open(self.filename, 'wb') as file:
            file.write(data)

    def readData(self) -> bytes:
        with open(self.filename, 'rb') as file:
            data = file.read()
        return data

