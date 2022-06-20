from DataSource.DataSource import CompressionDecorator, EncryptionDecorator, FileDataSource

if __name__ == "__main__":
    records = "Name,Salary\nJohn Smith,100000\nSteven Jobs,912000"
    encoded = CompressionDecorator(EncryptionDecorator(FileDataSource("output.txt")))
    encoded.write_data(records)
    plain = FileDataSource("output.txt")
    
    print(records)
    print(plain.read_data())
    print(encoded.read_data())