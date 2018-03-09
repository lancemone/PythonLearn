# 函数嵌套  在函数内部再定义函数
x = 0  # 全局变量


def outside():  # 定义函数
    x = 1  # 局部变量，内嵌函数的外部变量

    def inside():  # 定义内嵌函数
        x = 2
        return x

    # 函数的返回值不仅可以返回多个，而且可以返回内嵌函数（这是闭包）
    return x, inside  # 返回变量值和函数


a, b = outside()  # 通过两个变量接收outside函数的返回值x和inside
print(x)  # 显示输出结果为：0
print(a)  # 显示输出结果为：1
# 返回内嵌函数时，如果函数名称后方没有加上“()”，调用外层函数时不会立即执行返回的函数，需要在调用外层函数后，添加“()”来执行
print(b())  # 显示输出结果为：2 ，不加()输出结果：<function outside.<locals>.inside at 0x1045388c8>
# 外层函数有多个返回值时，通过对外层函数返回值列表进行索引，找到函数执行
print(outside()[1]())


# 外层函数仅有一个返回值，在函数名称后方直接加‘()()’去执行返回的函数


# 在外层函数返回内嵌函数时，在函数名称后方加上了“()”，会在调用外层函数时自动执行
def outside1():
    print('执行外层函数')

    def inside1():
        print('执行内层函数')

    return inside1


outside1()  # 执行外层函数


def outside2():
    print('执行外层函数')

    def inside2():
        print('执行内层函数')

    return inside2()


outside2()  # 执行外层函数    执行内层函数

# 作用域
'''
作用域也叫命名空间，命名空间是一个我们看不到的字典，字典的键记录变量的名称，字典的值记录着变量的值。

每个模块都会创建一个全局命名空间，用于记录模块的变量，包括全局变量和局部变量，以及其它导入模块中的变量。

每个函数调用时都会创建一个局部命名空间，用于记录函数的变量，包括函数的参数和函数内部创建的变量。

另外，还有内置命名空间，任何模块都能够访问，记录了内置函数和异常。
'''
'''
全局变量的作用域是当前模块内
局部变量的作用域是函数或者内嵌函数中，当在函数中创建与全局变量同名的局部变量时，在函数内部会自动屏蔽同名的全局变量'''

# 读取和修改全局变量
radius = float(input('请输入圆的半径：'))  # 创建半径的变量并赋值


def get_perimeter():
    perimeter = round(2 * 3.14 * radius, 2)  # 一般情况下可以在函数直接读取全局变量（2表示保留小数点后两位）
    return perimeter


print(get_perimeter())


# 利用内置函数globals来读取同名的全剧变量
def global_case():
    radius = 3.14
    result = radius * globals()['radius']  # 通过globals函数获取全局变量
    return result


print(global_case())


# 在函数中修改全局变量（或者叫重新绑定全局变量为其他值）
def change_global():
    global radius  # 声明要修改的全局变量
    radius = 4  # 修改变量值


change_global()  # 调用函数
print(radius)


# 在内嵌函数中修改外层函数中的局部变量，可以使用关键字nonlocal进行声明。使用方法和关键字global类似
def nonlocal_case():
    x = 10  # 创建局部变量

    def change_nonlocal():  # 定义函数
        nonlocal x  # 声明要修改的外部变量
        x = 5  # 修改变量值

    change_nonlocal()  # 调用修改函数执行修改
    return x  # 返回变量x的值


print(nonlocal_case())  # 显示输出局部变量x的值，结果为：5


# 闭包（closure）：闭包由要执行的代码块（内嵌函数）和为自由变量（外部变量）提供绑定的计算环境（作用域/命名空间）组成。
# 闭包就是由返回的内嵌函数和这个内嵌函数中用到的外部变量（1）以及其他函数（2）打包而成的一个整体
def synthesis():
    count = int(input('请放入宝石:'))
    while True:
        if count < 3:
            count += int(input('宝石太少，请在放入一些宝石：'))
        else:
            break

    def execute():
        result = count // 3  # 调用外部变量进行整除运算
        print('您放入了%s颗宝石，合成了%s颗高级宝石' % (count, result))

    return execute()  # (return execute)


exe = synthesis()
print('------------------开始合成------------------')
exe  # 执行闭包内容   (exe())
