# 默认情况下，Python中的成员函数和成员变量都是公开的(public),在python中没有类似public,private等关键词来修饰成员函数和成员变量
# 在python中定义私有变量只需要在变量名或函数名前加上 ”__“两个下划线，那么这个函数或变量就是私有的了
# 在内部，python使用一种 name mangling 技术，将 __membername替换成 _classname__membername，也就是说，类的内部定义中,所有以双下划线开始的名字都被"翻译"成前面加上单下划线和类名的形式

# python中的私有变量和私有方法仍然是可以访问的；访问方法如下：
# 私有变量:实例._类名__变量名
# 私有方法:实例._类名__方法名()

# 其实，Python并没有真正的私有化支持，但可用下划线得到伪私有。
# （1）_xxx      "单下划线 " 开始的成员变量叫做保护变量，意思是只有类实例和子类实例能访问到这些变量，
# 需通过类提供的接口进行访问；不能用'from module import *'导入
# （2）__xxx    类中的私有变量/方法名 （Python的函数也是对象，所以成员方法称为成员变量也行得通。）,
# " 双下划线 " 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
# （3）__xxx__ 系统定义名字，前后均有一个“双下划线” 代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数。

class A(object):
    def __init__(self):
        self.__data = []  # 翻译成 self._A__data=[]

    def add(self, item):
        self.__data.append(item)  # 翻译成 self._A__data.append(item)

    def printData(self):
        print(self.__data)  # 翻译成 self._A__data


a = A()
a.add('hello')
a.add('python')
a.printData()
# print a.__data  #外界不能访问私有变量 AttributeError: 'A' object has no attribute '__data'
print(a._A__data)  # 通过这种方式，在外面也能够访问“私有”变量；这一点在调试中是比较有用的！
