
import base64
import zlib
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, name):
        self.name = name

    def write_data(self, data):
        with open(self.name, "w", encoding="utf-8") as f:
            f.write(data)

    def read_data(self):
        with open(self.name, 'r', encoding="utf-8") as f:
            return f.read()


class DataSourceDecorator(DataSource):
    def __init__(self, source):
        self.wrappee = source

    def write_data(self, data):
        self.wrappee.write_data(data)

    def read_data(self):
        self.wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        super().write_data(self.encode(data))

    def read_data(self):
        self.decode(super().read_data())

    def encode(self, data):
        data_bytes = data.encode('utf-8')
        data_base64 = base64.b64encode(data_bytes)
        data_base64_str = data_base64.decode('utf-8')
        return data_base64_str

    def decode(self, data):
        data_bytes = base64.b64decode(data)
        data_decoded = data_bytes.decode('utf-8')
        return data_decoded


class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data):
        super().write_data(self.compress(data))

    def read_data(self):
        self.decompress(super().read_data())

    def compress(self, data):
        data_bytes = data.encode("utf-8")
        compress_data = zlib.compress(data_bytes)
        print(compress_data, type(compress_data))
        compress_data_str = compress_data.decode("zlib_codec")
        return compress_data_str

    def decompress(self, data):
        data_bytes_str = data.encode()
        data_bytes = zlib.decompress(data_bytes_str)
        data_decompressed = data_bytes.decode()
        return data_decompressed
