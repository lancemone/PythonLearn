# 自定义函数
# 编程的过程中，往往要写一些进行某种运算的代码，通过这些代码获取我们想要的结果。这些运算的代码，我们需要使用到多次，为了避免大量重复编写这些代码，我们可以把这些运算过程的代码定义为函数。
# 定义函数的关键字：def
def get_birthday0(id0):  # 定义函数名称并设定参数
    birthday = id0[6:14]  # 函数运算过程
    print(birthday)  # 函数运算过程


get_birthday0('110123199001012121')  # 调用函数，显示输出结果为：19900101
get_birthday0('120122199508081321')  # 调用函数，显示输出结果为：19950808

'''
1、要使用def这个关键字进行定义。

2、函数的名称建议使用小写单词组成，单词间以下划线分隔（下划线命名法），这样比较方便理解函数名称的含义。

3、参数是一个自定义的变量名称，通常也是使用小写的单词，用于提示输入的参数内容。

4、定义参数名称与参数以“：”结尾。

5、在定义函数名称与参数的下方，向右缩进编写运算代码的语句块。

6、通过函数名称并写入相应的参数即可调用函数，以实现相应的运算。'''


# 在函数中返回结果
def get_birthday1(id1):  # 定义函数名称并设定参数
    birthday1 = id1[6:14]  # 函数运算过程
    return birthday1  # 返回运算结果。如果不加入return语句，则函数默认执行return None，即函数返回结果为None


# retrun语句会跳出结束函数，并返回结果，该语句之后的语句将不再被执行。

a = get_birthday1('140424199603028797')  # 调用函数
print('birthday is %s' % a)  # 显示输出结果


# 在函数中返回多个结果
def get_birthday2(id2):
    year = id2[6:10]
    month = id2[10:12]
    day = id2[12:14]
    return year, month, day  # 返回多个结果


y, m, d = get_birthday2('161518199803051231')  # 调用函数，返回值赋予三个变量
print('birthday is %s-%s-%s' % (y, m, d))
b = get_birthday2('181629189203231921')  # 可以通过1个变量接收函数的返回结果，这时我们得到的是1个包含了3个元素元组。
print('birthday is %s-%s-%s' % b)


# 定义一个根据输入参数返回一个列表的函数
def creat_name_list(name_list, name1, name2, name3):
    name_list.append(name1)  # 为列表添加元素
    name_list.append(name2)
    name_list.append(name3)

lst = []  # 创建空列表
creat_name_list(lst, 1, 2, 3)  # 这样的操作仅限于可变的数据结构，而数字、字符串以及元组是不能够被改变的，所以无法进行这样的修改。
print(lst)  # 输出[1， 2， 3]


# 收集参数  定义可接受任意数量参数的函数
def creat_name_lst(name_lst, *names):
    print(type(names))  # 显示输出参数names的数据类型，结果为：<class 'tuple'>
    if names is not None:  # 判断收集参数names不为空值
        for name in names:  # 循环遍历names
            name_lst.append(name)  # 为列表添加新元素

lst1 = []
creat_name_lst(lst1, 1, 2, 3, 4, 5, 6)
print(lst1)


# 在函数内部创建列表然后返回
def creat_name_lst1(*names):
    name_lst1 = list(names)
    return name_lst1


lst1_1 = creat_name_lst1(1, 2, 3, 4)
print(lst1_1)


def avg(first, *rest):  # 使用一个*参数让一个函数接受任意数量的位置参数,*只能解析可迭代序列
    return (first + sum(rest)) / (1 + len(rest))  # rest是由所有其他位置参数组成的元组。然后我们在代码中把它当成了一个序列来进行后续的计算。
print(avg(1, 2))  # 1.5
print(avg(1, 2, 3, 4))  # 2.5

import html
# 使用两个**开头的参数使函数接受任意数量的关键字参数
def make_element(name, value, **attrs):  # 在这里，attrs是一个包含所有被传入进来的关键字参数的字典。
    keyvals = ['%s = "%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))



def anyargs(*args, **kwargs):  # 能同时接受任意数量的位置参数和关键字参数
    print(args)  # A tuple
    print(kwargs)  # A dict


# * 或 ** 另一种用法
def user_info(name, age, height, sex):
    info = 'name:%s age:%s height:%s sex:%s' % (name, age, height, sex)
    return info


lou = {'name': 'xiaolou', 'age': '18', 'height': '180', 'sex': 'male'}  # 创建参数字典
print(user_info(**lou))  # 调用函数，并传入参数

s1 = {(1, 2, 3), (3, 4, 5)}
s2 = {*(1, 2, 3), *(3, 4, 5)}
print(s1)  # 显示输出结果为：{(3, 4, 5), (1, 2, 3)}
print(s2)  # 显示输出结果为：{1, 2, 3, 4, 5}




# 一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数。 有一点要注意的是，在*参数后面仍然可以定义其他参数。


# 定义只接受关键字参数的函数
# 将强制关键字参数放到某个*参数或者单个*后面使某些参数强制使用关键字参数传递
def recv(maxsize, *, block):
    'Receives a message'
    pass


recv(1024, True)  # TypeError
recv(1024, block=True)  # Ok


# 在接受任意多个位置参数的函数中指定关键字参数
def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip \
            if clip > m else m
    return m


print(mininum(1, 2, 4, -5, -7, 9))
print(mininum(1, 2, 4, -5, -7, 9, clip=-10))
print(mininum(1, 2, 4, -5, -7, 9, clip=0))


# 给函数参数增加元信息：为函数的参数增加一些额外的信息，使其他使用者能清楚的知道这个函数应该怎么使用
# 函数参数注解
# python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距
def add(x: int, y: int) -> '加法程序':  # 可以使用任意类型的对象给函数添加注解(例如数字，字符串，对象实例等等)
    return x + y


help(add)


# 构建返回多个值的函数
def myfun():
    return 1, 2, 4  # 为返回多个值，可直接return一个元组


aa, bb, cc = myfun()
mf = myfun()
print(aa, bb, cc, mf)


# 定义有默认参数的函数
def spam1(a, b=43):  # 定义一个有可选参数的函数直接在函数定义中给参数指定一个默认值，并放到参数列表最后
    print(a, b)


print(spam1(1))  # a=1 b=43
print(spam1(1, 4))  # a=1 b=4


# 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值
def spam2(a2, b2=None):
    if b2 is None:
        return b2
    return a2


# 不赋予默认值，仅测试默认参数是不是有传递进来
_no_value = object()


def spam3(a3, b3=_no_value):
    if b3 is _no_value:
        print('No b3 value supplied')
    else:
        print(b3)


spam3(1)  # No b3 value supplied
spam3(1, 3)  # 输出3
spam3(2, None)  # 输出None

# 默认参数的值仅仅在函数定义的时候赋值一次
x = 42


def spam(a, b=x):
    print(a, b)


spam(1)  # 1 42
x = 23  # 当改变x的值的时候对默认参数值并没有影响，因为在函数定义的时候就已经确定了它的默认值了
spam(1)  # 1 42


# 默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串
def spam(a, b=[]):  # 最好是将默认值设为None，否则会产生其他问题
    print(b)
    return b


x = spam(1)  # 输出 []
x.append(99)
print(x)  # 输出99
spam(1)  # 输出99



# 通过设定一个参数来控制函数返回结果
# 设置默认值的参数我们叫它关键字参数，没有默认值的参数是位置参数。关键字参数对位置没有要求，不管是设定参数还是调用函数时，可以任意顺序写入。位置参数必须有着严格的位置和顺序，这样才能在调用函数时一一对应。
def get_birthday(id, get_age=False):  # 定义函数名称并设定参数,get_age为关键字参数,默认值为False.若只定义参数而不写入默认值，即便函数运算过程中没有使用这个参数，程序也会抛出异常

    if get_age:  # 对参数进行判断,如果输入的参数为True，执行if语句；如果没有输入参数则按照默认参数False
        return 2018 - int(id[6:10])
    else:
        year = id[6:10]
        month = id[10:12]
        day = id[12:14]
        return year, month, day


bir = get_birthday('181281199812142412', True)
print(bir)  # 执行if语句
bir0 = get_birthday('181281199812142412')  # 执行else语句


# 抛出异常 我们定义的函数，往往对输入的参数有类型的要求，当输入了错误的类型，会有异常发生
def subtraction(num1, num2):
    # 使用内置函数isinstance()对输入的参数值进行类型的比较，当任何一个参数不是int（整数）或者float（小数）类型时，都将抛出异常。
    if not isinstance(num1, (int, float)) \
            or not isinstance(num2, (int, float)):  # 判断参数是否为指定类型，代码过长时使用 \ 换行
        raise TypeError('参数类型错误，参数必须为整数或小数。')  # 关键字raise用于引发异常，TypeError()为异常类型，括号中可以输入自定义的异常提示

    result1 = num1 - num2
    return result1


print(subtraction(5, 3))
print(subtraction('5', 3))  # 参数类型错误，程序抛出异常


# 定义空函数  空函数一般是在还没有确定函数内部代码如何编写，但是又需要不影响程序运行时使用。
def subtraction1(num1, num2):  # 定义函数并设定参数
    pass  # 使用pass占位，保证程序运行正常


print(subtraction1(1, 2))  # 调用函数，返回结果为：None。


# 函数说明 如果想为函数添加说明文档，除了使用“#”进行注释，还可以在def语句后面直接写入说明字符串。
def get_area(width, height):
    '这是一个计算面积的函数。'
    return width * height


# 当一个函数添加了文档，我们可以通过调用函数的__doc__属性查看文档。
print(get_area.__doc__)  # 显示输出结果为：这是一个计算面积的函数。
help(get_area)  # 还可以使用内置函数help()进行查看
