from decorators.DataSource import DataSource

class FileDataSource(DataSource):
    def __init__(self, name):
        self.__name = name
    def writeData(self, data:bytes):
        f = open(self.__name, "w")
        f.write(str(data))
        f.close()
    def readData(self):
        f = open(self.__name, "r")
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
        f.close()
    