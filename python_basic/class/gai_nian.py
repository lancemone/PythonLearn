# 类的概念：类是某一种对象的总称，它包含从某一种对象中抽取出来的相同或相像的全部特性。

# 定义类。格式：class 类名称(超类名称):超类是指当前的类所继承的类，如果没有继承超类括号部分可以省略。
# 类的定义实际上就是执行代码块，而不仅仅是在类的里面定义方法。

class Human:  # 类的名称一般会使用首字母大写的单词
    def set_name(self, user_name):  # 类的函数
        self.name = user_name  # 修改类的变量

    def get_name(self):
        return self.name  # 返回类的变量

    def say_hello(self):
        print('Hi! My name is %s' % self.name)  # 使用类的特性


# 实例化，调用类
persion01 = Human()
persion01.set_name('lance')
persion01.say_hello()  # 输出结果 Hi! My name is lance

persion02 = Human()
persion02.set_name('olivia')
persion02.say_hello()  # 输出结果 Hi! My name is olivia

# 封装  将抽象得到的全部特性结合为一个整体（也可以看做将数据和操作捆绑到一起），形成类即为封装
# 封装后，所有特性都是类的成员，除此之外，封装还是达到接口与实现分离的过程
# 封装，即隐藏对象的特性和实现细节（实现），仅对外提供可调用的特性（接口），将访问控制在只能够对被允许的对特性进行读与修改的级别

# 未封装类 虽然是两个实例对象，并且调用每个实例对象自己的方法取名字，但是他们的set_name()方法都修改同一个全局变量，这样就会互相干扰
global_name = ''  # 创建全局变量并赋值


class Human1(object):
    def set_name(self, name):
        global global_name
        global_name = name

    def get_name(self):
        return global_name

    def say_hello(self):
        print('Hi! My name is %s' % global_name)


persion11 = Human1()
persion11.set_name('lance')
persion12 = Human1()
persion12.set_name('olivia')
persion11.say_hello()  # 输出结果 Hi! My name is olivia
persion12.say_hello()  # 输出结果 Hi! My name is olivia


# 函数和方法的区别

class MyClass:
    """A simple example class（一个简单的示例类）"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()

print(x.f)  # 显示输出结果为：<bound method MyClass.f of <__main__.MyClass object at 0x000000000265D630>>
print(MyClass.f)  # 显示输出结果为：<function MyClass.f at 0x000000000265FA60>
'''实例对象有效的方法名取决于类。根据定义，类的所有特性中，函数对象都是在定义其实例中相应的方法。所以，在我们的例子中，x.f将是一个有效的方法调用，
因为MyClass.f是一个函数。但是x.i不是有效的方法调用，因为MyClass.i不是一个函数。但是，x.f和MyClass.f不同，x.f是一个方法对象，而不是一个函数对象

可以理解：绑定到实例对象特性上的函数就是方法。

另外，还有一个区别在于类的函数与实例方法的第一个参数是“self”。

参数“self”绑定到了方法所属的实例，通过参数“self”我们能够访问实例对象的特性。

也正是因为如此，通过实例调用方法时，这个参数不需要提供。

而通过类调用函数的时候，参数“self”需要提供，如果访问类的特性填入类名称，如果访问实例特性填入实例名称。

'''
Human.set_name(Human, '明步')  # 设置类的特性,如果调用时，我们不输入Human这个参数，则会抛出异常。
Human.say_hello(Human)  # 显示输出结果为：嗨！大家好，我是明步！


# 私有化


# 类的命名空间，所有在类中定义的代码都会在独立的命名空间中执行，也就是类的命名空间（class namespace）
# 这个命名空间，可以由类的所有成员（类的实例）进行访问

class Register:  # 创建注册类
    reg_count = 0  # 定义计数变量

    def register(self):  # 定义计数方法
        Register.reg_count += 1  # 累加注册数写入计数变量
        print('当前注册人数为%s人' % Register.reg_count)


# 每一个实例都可以调用自身的方法对类的计数变量进行访问
reg1 = Register()  # 类实例化
reg1.register()

reg2 = Register()
reg2.register()

# 绑定
reg1.reg_count = 0  # 修改变量值
print(reg1.reg_count)  # 示输出结果为：0
print(reg2.reg_count)  # 示输出结果为：2


# 修改后并没有让类的变量发生变化，而是实例自身的变量产生了变化，其他实例的变量值并不会发生变化


# 继承：当一个对象所属的类是另一个对象所属的类的子集时，它就是后者的子类（subclass)，而后者是前者的超类（superclass），或叫做父类、基类。
# 在面向对象的程序设计中，子类的关系是隐藏的。类的定义取决于它的所有支持的方法。子类也会包含超类中的这些方法（但是看不到）
# 定义子类要做的只是定义更多特性的过程或者重写（override）超类中已有的特性。
# 子类包含父类的所有特性；子类中能够对超类的特性进行重写；子类能够添加父类中不存在的特性。

class Shielding:  # 创建屏蔽类
    def __init__(self):  # init()这个方法，它是无需调用自动执行的方法
        self.words = []  # 屏蔽内容列表
        self.symbol = ''  # 屏蔽后显示的符号

    def change(self, sentence):  # 定义修改屏蔽词的方法
        string = sentence
        for word in self.words:  # 遍历屏蔽词列表
            if word in sentence:
                string = string.replace(word, self.symbol * len(word))
        return string


class ShieldingWords(Shielding):  # 创建屏蔽词类
    def __init__(self):  # 重写超类的init方法
        self.words = ['银行', '账号', '密码']  # 设置屏蔽词列表
        self.symbol = '*'


class ShieldingSymbols(Shielding):  # 创建屏蔽字符类
    def __init__(self):
        self.words = '#'
        self.symbol = '@'

    def message(self):
        print('禁止在邮箱地址中使用%s,已使用%s代替' % (self.words, self.symbol))


s = Shielding()
print(s.change('你银行的账号和密码是什么？'))  # 显示输出结果为：你银行的账号和密码是什么？
w = ShieldingWords()
print(w.change('你银行的账号和密码是什么？'))  # 显示输出结果为：你**的**和**是什么？
c = ShieldingSymbols()
print(c.change('我的邮箱是4907442#qq.com'))  # 显示输出结果为：我的邮箱是4907442@qq.com
c.message()  # 显示输出结果为：禁止在邮箱地址中使用"#"，已使用"@"代替！

# 查验继承关系：使用issubclass(class, classinfo)函数
print(issubclass(ShieldingWords, Shielding))  # 显示输出结果为：True
print(issubclass(Shielding, ShieldingWords))  # 显示输出结果为：False
# 使用类的__bases__特性来查看谁是子类的超类
print(ShieldingWords.__bases__)  # 显示输出结果为：(<class '__main__.Shielding'>,)
# 调用__class__特性知道某个对象是哪个类的实例
s = ShieldingWords()
print(s.__class__)  # 显示输出结果为：<class '__main__.ShieldingWords'>
