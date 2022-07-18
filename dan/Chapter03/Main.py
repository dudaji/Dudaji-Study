from decorators.CompressionDecorator import CompressionDecorator
from decorators.EncryptionDecorator import EncryptionDecorator
from decorators.FileDataSource import FileDataSource

if __name__ == "__main__":
    salaryRecords = "Name,Salary\nJohn Smith,100000\nSteven Jobs,912000"
    file = "out/OutputDemo.txt"
    encoded = CompressionDecorator(
                EncryptionDecorator(
                  FileDataSource(file)))
    encoded.setCompressionLevel(0)
    encoded.writeData(salaryRecords)
    plain = FileDataSource(file)

    print("----input----")
    print(salaryRecords)
    print("----Encoded----")
    print(plain.readData())
    print("----Decoded----")
    print(encoded.readData())
    