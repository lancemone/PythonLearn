# 数据属性
# 类数据属性和实例数据属性
class persion_1(object):
    '''persion类的注释'''
    tall = 180
    hobbies = []

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def inmofa(self):
        print('%s is %s weights %s' % (self.name, self.age, self.weight))


persion_1.hobbies.extend(['football', 'women'])  # 类属性数据属于类本身，可以通过类名访问/修改
Bruce = persion_1('Bruce', 23, 43)
Bruce.tall = 190  # 重新赋值或修改
print(Bruce.tall)
print(persion_1.__dict__)
print(Bruce.__dict__)
del Bruce.tall  # 再次删除实例的赋值
print(persion_1.tall, Bruce.tall)

Bruce.tall += 3
print(persion_1.tall, Bruce.tall)
print(persion_1.__dict__)
print(Bruce.__dict__)
del Bruce.tall
print(Bruce.__dict__)

print(persion_1.hobbies is Bruce.hobbies)
Bruce.hobbies = ['python']
print(persion_1.__dict__)
print(Bruce.__dict__)
# del Bruce.hobbies
print(persion_1.hobbies, Bruce.hobbies)

Bruce.hobbies.append('CS')
print(persion_1.hobbies, Bruce.hobbies)
