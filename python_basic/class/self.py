# 类的方法中的self参数详解
# self是一种约定。在Python中，类方法的第一个参数表示对象本身，在Python中一般使用self。
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self

# 函数分为静态函数，类函数，成员函数
# 静态函数(@staticmethod): 即静态方法,主要处理与这个类的逻辑关联, 如验证数据;
# 类函数(@classmethod):即类方法, 更关注于从类中调用方法, 而不是在实例中调用方法, 如构造重载;
# 成员函数: 实例的方法, 只能通过实例进行调用;

# self的原理：假如你有一个类称为MyClass和这个类的一个实例MyObject。当你调用这个对象的方法MyObject.method(arg1, arg2)的时候，这会由Python自动转为MyClass.method(MyObject, arg1, arg2)
# 这意味着如果你有一个不需要参数的方法，你还是得给这个方法定义一个self参数
class Persion:
    def sayHi(self):
        print('Hello, how are you')


p = Persion()
p.sayHi()  # Hello,how are you
Persion.sayHi(p)  # 结果同上


# 去掉self
class Person1:
    def sayHi():
        print('Hello,how are you?')


p1 = Person1()
Person1.sayHi(p1)
p.sayHi()  # 报错 TypeError: sayHi() takes 0 positional arguments but 1 was given
