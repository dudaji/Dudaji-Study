from abc import ABC, abstractmethod

class DataSource(ABC):

    @abstractmethod
    def writeData(self, data: bytes) -> None:
        pass

    @abstractmethod
    def readData(self) -> bytes:
        pass
