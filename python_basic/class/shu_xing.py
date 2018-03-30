# 数据属性
# 类数据属性和实例数据属性
class persion_1(object):
    '''persion类的注释'''
    tall = 180  # 不可变类型类属性
    hobbies = []  # 可变类型类属性

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def inmofa(self):
        print('%s is %s weights %s' % (self.name, self.age, self.weight))


persion_1.hobbies.extend(['football', 'women'])  # 类属性数据属于类本身，可以通过类名访问/修改
print(persion_1.hobbies)
# class can add class attribute after class defination
persion_1.hobbies1 = ['reading', 'swimming']  # 在类定义后可以通过类名动态添加类数据属性，新增的类属性也被类和所有实例共有
print(persion_1.hobbies1)
print(dir(persion_1))  # 通过内建函数dir()，或者访问类的字典属性’_ _dict _ _’这两种方式都可以查看类有哪些属性

lance = persion_1('lance', 23, 54)  # 实例数据属性只能通过实例访问
print(lance.name, lance.age)
# class instance can add new attribute
# "gender" is the instance attribute only belongs to wilber
lance.gender = 'male'  # 实例生成后还可以动态添加实例数据属性，但是实例数据属性只属于该实例，其他实例不拥有该数据属性
print(lance.gender)
# class instance can access class attribute
lance.hobbies.append('python')  # 实例可以访问/修改类数据属性
print(lance.hobbies)
'''
对于类数据属性和实例数据属性，可以总结为：

类数据属性属于类本身，可以通过类名进行访问/修改
类数据属性也可以被类的所有实例访问/修改
在类定义之后，可以通过类名动态添加类数据属性，新增的类属性也被类和所有实例共有
实例数据属性只能通过实例访问
在实例生成后，还可以动态添加实例数据属性，但是这些实例数据属性只属于该实例'''

# 特殊类属性:对于所有的类，都有一组特殊的属性
'''
_ _ name_ _：类的名字（字符串）
_ _ doc _ _ ：类的文档字符串
_ _ bases _ _：类的所有父类组成的元组
_ _ dict _ _：类的属性组成的字典
_ _ module _ _：类所属的模块
_ _ class _ _：类对象的类型'''
print(persion_1.__name__)  # persion_1
print(persion_1.__doc__)  # persion类的注释
print(persion_1.__bases__)  # (<class 'object'>,)
print(persion_1.__dict__)
print(persion_1.__module__)  # __main__
print(persion_1.__class__)  # <class 'type'>

# 隐藏属性：类数据属性属于类本身，被所有该类的实例共享；并且，通过实例可以去访问/修改类属性。但是，在通过实例中访问类属性的时候一定要谨慎，因为可能出现属性”隐藏”的情况
Bruce = persion_1('Bruce', 23, 43)
# 当通过实例赋值/修改不可变属性的时候，将为实例Bruce新建一个tall实例属性，这时，”person.tall is not Bruce.tall”
Bruce.tall = 190  # 重新赋值或修改
print(Bruce.tall)
print(persion_1.__dict__)
print(Bruce.__dict__)
# 当通过”del Bruce.tall”语句删除实例的tall属性后，再次成为”person.tall is Bruce.tall”
del Bruce.tall  # 再次删除实例的赋值
print(persion_1.tall, Bruce.tall)

Bruce.tall += 3
print(persion_1.tall, Bruce.tall)
print(persion_1.__dict__)
print(Bruce.__dict__)
del Bruce.tall
print(Bruce.__dict__)

print(persion_1.hobbies is Bruce.hobbies)
# 当通过实例赋值可变属性的时候，都将为实例Bruce新建一个books实例属性
Bruce.hobbies = ['python']
print(persion_1.__dict__)
print(Bruce.__dict__)
# del Bruce.hobbies
print(persion_1.hobbies is Bruce.hobbies)  # 输出：['football', 'women'] ['python']

# 当通过实例修改hobbies属性的时候，将修改Bruce. hobbies指向的内存地址（即person.hobbies），此时，”person.hobbies is not Bruce. hobbies”
Bruce.hobbies.append('CS')
print(persion_1.hobbies, Bruce.hobbies)  # 输出：['football', 'women', 'CS'] ['football', 'women', 'CS']

# 注意，虽然通过实例可以访问类属性，但是，不建议这么做，最好还是通过类名来访问类属性，从而避免属性隐藏带来的不必要麻烦
