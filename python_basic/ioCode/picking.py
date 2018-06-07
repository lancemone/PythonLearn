# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling.反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上

import pickle
import os

d = dict(name='motao', age=21)
d = dict(name='taomo', age=21)
bb = pickle.dumps(d)  # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
print(bb)
print(pickle.loads(bb))  # 反序列化出对象

f = open('dump.txt', 'wb')
pickle.dump(d, f)  # 直接把对象序列化之后写入一个file
f.close()
ff = open('dump.txt', 'rb')
dd = pickle.load(ff)
ff.close()
print(dd)

os.remove('/Users/taomo/PycharmProjects/PythonLearn/simple_project/dump.txt')

import json

# json格式的序列化
json_dict = dict(name='Bob', age=12)
print(json.dumps(json_dict))

# json格式反序列化为Python对象
json_str = '{"name":"Bob", "age":12}'
print(json.loads(json_str))


# 用class表示对象并序列化
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('lance', 14)


# 默认情况下类的实例对象不是一个可序列化的JSON对象，dumps方法无法将Student实例变为一个JSON{}对象
# 写一个转换函数将类的实例对象转换为dict
def s_to_dict(std):
    return {
        'name': std.name,
        'age': std.age
    }


print(json.dumps(s, default=s_to_dict))  # 可选参数default会把任意一个对象变成一个可序列为JSON的对象,通过转换函数传入

# 把任意class实例变为dict
ss = Student('mone', 14)
print(json.dumps(ss, default=lambda
    obj: obj.__dict__))  # 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class

# json反序列化为类实例对象
json_str = '{"age":14, "name":"sannas"}'


def json_to_class(d):
    return Student(d['name'], d['age'])


print(json.loads(json_str, object_hook=json_to_class))

# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)  # ensure_ascii参数会将中文转换为16进制
print(s)
