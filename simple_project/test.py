class A(object):
    def __init__(self):
        self.__data = []

    def add(self, item):
        self.__data.append(item)

    def printData(self):
        print(self.__data)


a = A()
a.add('hello')
a.add('python')
a.printData()
# print(a.__data)
print(a._A__data)
