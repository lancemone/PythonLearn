# 在一个类中，可能出现三种方法，实例方法、静态方法和类方法

# 实例方法：实例方法的第一个参数必须是”self”，实例方法只能通过类实例进行调用，这时候“self”就代表这个类实例本身。通过”self”可以直接访问实例的属性。
class person(object):
    tall = 180
    hobbies = []

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def infoma(self):
        print('%s is %s weights %s' % (self.name, self.age, self.weight))


Bruce = person("Bruce", 25, 180)
Bruce.infoma()


# 类方法：一个只在类中运行而不在实例中运行的方法。类方法以cls作为第一个参数，cls表示类本身，定义时使用@classmethod装饰器。通过cls可以访问类的相关属性
class persion1(object):
    tall = 180
    hobbies = []

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @classmethod  # 类的装饰器
    def infoma(cls):  # cls表示类本身，使用类参数cls
        print(cls.__name__)
        print(dir(cls))


# person1.infoma()   直接调用类的装饰器函数，通过cls可以访问类的相关属性
Lance = persion1('Lance', 25, 180)  # 也可以通过两步骤来实现，第一步实例化，第二步调用装饰器
Lance.infoma()


# 类方法的使用：好处是以后重构类的时候不必要修改构造函数，只需要额外添加函数然后使用装饰符@classmethod就可以了
# 定义一个时间类
class Data_test(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        print(self.year)
        print(self.month)
        print(self.day)


t = Data_test(2013, 2, 4)
t.out_date()

'''如果用户输入的是2014-12-23这样的字符格式，那么就需要在调用Data_test类前做一下处理
string_data = '2014-12-23'
year, month, day = map(int, string_date.split('-'))
s = Data_test(year, month, day)
先将2014-12-23分解成year,month,day三个变量，然后转换成int，在调用Data_test类
'''


# 使用类函数将字符串处理函数放在类中
class Data(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def get_date(cls, string_date):
        year, month, day = map(int, string_date.split('-'))
        date1 = cls(year, month, day)
        return date1

    def out_date(self):
        print(self.year, self.month, self.day)


d = Data.get_date('2014-12-23')
d.out_date()


# 静态方法：静态方法没有参数限制，既不需要实例参数，也不需要类参数，定义的时候使用@staticmethod装饰器。
# 同类方法一样，静态法可以通过类名访问，也可以通过实例访问
class Persion_1(object):
    tall = 180
    hobbies = []

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @staticmethod
    def infoma():
        print(Persion_1.tall, Persion_1.hobbies)


Persion_1.infoma
Luna = Persion_1('Luna', 23, 42)
Luna.infoma()

# 类的专有方法：
'''
内置方法：Python中声明每一个类系统都会加上一些默认内置方法，提供给系统调用该类的对象时使用。比如需要实例化一个对象时，需要调用该类的init方法；使用print去打印一个类时，其实调用的是str方法等等。
__init__       构造函数，在生成对象时调用
__del__        析构函数，释放对象时使用
__repr__       打印，转换
__setitem__    按照索引赋值
__getitem__    按照索引获取值
__len__        获得长度
__cmp__        比较运算
__call__       函数调用
__add__        加运算
__sub__        减运算
__mul__        乘运算
__div__        除运算
__mod__        求余运算
__pow__        称方


init(self, …)：初始化对象class，在创建新对象时调用。在方法里，可以初始化该对象的属性，否则调用其他时可能出“现has no attribute”错误；
del(self)：释放对象，在对象被虚拟机删除之前调用；
new(cls,*args,**kwd)：实例的生成操作，相比init在对象实例化调用做初始化，new方法运行在实例化阶段，修改某些实例化过程；
str(self)：在使用print语句时被调用，将对象的属性值拼接成字符串返回；
getitem(self, key)：获取序列的索引key对应的值，需要使用[]操作符的类需要覆盖的，等价于seq[key]；
setitem(self, key, value)：类似geitem，需要seq[key]=value操作的类需要实现该方法；
len(self)：在调用内联函数len()时被调用；
getattr(s, name)： 获取属性的值；
setattr(s, name, value)：设置属性的值；
delattr(s, name)： 删除name属性；
getattribute()：getattribute()功能与getattr()类似，无条件被调用，通过实例访问属性。如果class中定义了getattr()，则getattr()不会被调用（除非显示调用或引发AttributeError异常）；
gt(self, other)：判断self对象是否大于other对象；
lt(self, other)：判断self对象是否小于other对象；
ge(slef, other)：判断self对象是否大于或者等于other对象；
le(self, other)： 判断self对象是否小于或者等于other对象；
eq(self, other)：判断self对象是否等于other对象；
call(self, *args)： 把实例对象作为函数调用，在一个对象后面加上()，虚拟机就会调用该call方法。


内置变量
name：标识模块的名字的一个系统变量。假如当前模块是主模块（也就是调用其他模块的模块），那么此模块名字就是”main“，通过if判断这样就可以执行“main”后面的主函数内容；假如此模块是被import的，则此模块名字为文件名字（不加后面的.py），通过if判断这样就会跳过“main”后面的内容；
file：用来获得模块所在的路径的，这可能得到的是一个相对路径；
package：当前文件为None，导入其他文件，指定文件所在包用 . 分割；
doc：文件注释'''


# 使用类的内置方法进行方法构造
class persion_1():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def __cmp__(self):
        pow_age = self.age.__pow__(2)
        print(pow_age)

    def __len__(self):
        name_del = self.name.__len__()
        print(name_del)

    def __add__(self):
        adds = self.age.__add__(self.__weight)
        print(adds)

    def infoma(self):
        print('%s is %s weights %s' % (self.name, self.age, self.__weight))


print(persion_1.__class__)
print(persion_1.__repr__)

per = persion_1('lance', 23, 54)
print(per)
infome = per.infoma()
cmp = per.__cmp__()
lens = per.__len__()
adds = per.__add__()
print('doc is %s' % per.__doc__)
print('dir is %s' % per.__dir__)
print('delatter is %s' % per.__delattr__)
print('gt is %s' % per.__gt__)
print('hash is %s' % per.__hash__)
print('init is %s' % per.__init__)
print('new is %s' % per.__new__)
'''output:
<class 'type'>
<slot wrapper '__repr__' of 'object' objects>
<__main__.persion_1 object at 0x10668ba58>
lance is 23 weights 54
529
5
77
doc is None
dir is <built-in method __dir__ of persion_1 object at 0x10668ba58>
delatter is <method-wrapper '__delattr__' of persion_1 object at 0x10668ba58>
gt is <method-wrapper '__gt__' of persion_1 object at 0x10668ba58>
hash is <method-wrapper '__hash__' of persion_1 object at 0x10668ba58>
init is <bound method persion_1.__init__ of <__main__.persion_1 object at 0x10668ba58>>
new is <built-in method __new__ of type object at 0x100994560>
'''
