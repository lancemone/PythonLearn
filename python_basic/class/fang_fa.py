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


# 类方法的使用
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

'''
