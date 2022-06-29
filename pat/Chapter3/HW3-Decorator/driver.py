from FileDataSource import FileDataSource
from EncryptionDecorator import EncryptionDecorator
from CompressionDecorator import CompressionDecorator

def main():

    msg = b'Hello, world!\n'

    src1 = FileDataSource('testFile1')
    src1.writeData(msg)
    assert msg == src1.readData()

    src2 = EncryptionDecorator(FileDataSource('testFile2'))
    src2.writeData(msg)
    assert msg == src2.readData()

    src3 = CompressionDecorator(FileDataSource('testFile3'))
    src3.writeData(msg)
    assert msg == src3.readData()

    src4 = EncryptionDecorator(CompressionDecorator(FileDataSource('testFile4')))
    src4.writeData(msg)
    assert msg == src4.readData()

    src5 = CompressionDecorator(EncryptionDecorator(FileDataSource('testFile5')))
    src5.writeData(msg)
    assert msg == src5.readData()

    print(msg.decode())

if __name__ == '__main__':
    main()

