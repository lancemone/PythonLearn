# 迭代器：迭代器就是一段代码，这段代码能够根据需求，重复完成某些事情
# 这段代码由两部分组成，一部分是__iter__()方法，一部分是__next__()方法。

#  偶数迭代器
class Even:
    def __init__(self):
        self.even = 0  # 定义变量保存数值

    def __next__(self):  # 重写next方法
        self.even += 2  # 计算每次迭代的偶数
        return self.even

    def __iter__(self):  # 重写iter方法
        return self  # 返回实例对象为可迭代对象


even = Even()
# print(list(even))      # 想体验精尽人亡就取消这句代码的注释，然后运行......
for i in even:
    if i <= 12:
        print(i)
    else:
        break


# 通过迭代器获取一个有限数量列表
class Even1:
    def __init__(self, count):  # 定义获取次数的参数
        self.even = 0
        self.count = count  # 定义变量保存获取次数

    def __next__(self):
        if self.even < self.count * 2:  # 判断最优一次生成偶数小于最大的偶数
            self.even += 2
            return self.even
        else:
            raise StopIteration  # 到达指定数量停止迭代

    def __iter__(self):
        return self


even1 = Even1(10)  # 实例化并传入参数
print(list(even1))

# 内置函数iter()能够从可迭代对象中获取生成器，并通过内置函数next()逐一读取。
tup = (1, 2, 3, 4, 5)
ite = iter(tup)
for i in range(4):  # 注意：for语句不要写成“for i in ite”，因为这样也在调用迭代器取值，每个迭代器的值只能获取一次，取完为止
    print(next(ite))  # 输出结果为：1，2，3，4


# 生成器：生成器是通过函数实现的迭代器。yield（生产）这个关键词能够指定生成某个函数计算结果
# 写一个能从列表中获取所有能被3整除的数字生成器
def generate(lst):  # 定义生成器函数
    for i in lst:  # 循环遍历参数列表
        if i % 3 == 0:
            yield i  # 生成符合条件的数值


lst = [97, 19, 29, 72, 16, 93, 47, 92, 26, 75, 62, 89, 58, 10, 65, 63, 13, 52, 51, 60]
g = generate(lst)
while True:
    try:
        print(next(g))  # 通过内置函数逐一生成数值
    except:  # 捕获到异常时跳出循环
        break
for i in g:
    print(i)

# 生成器推导式（参考列表推导式,生成器推导式是写在两个圆括号“()”中
exp = (x for x in lst if x % 3 == 0)  # 通过生成器推导式定义生成器
print(list(exp))  # 使用内置函数list()将生成器转换为列表，显示输出结果为：[72, 93, 75, 63, 51, 60]


# 一个能够将嵌套列表中的所有元素取出生成非嵌套列表的生成器。
def generate1(lst1):
    for sublst in lst1:  # 循环遍历列表参数
        try:
            for num in sublst:  # 遍历循环参数列表的子列表
                yield num  # 生成符合条件的数值
        except:  # 如果sublst为单个数字会发生异常
            yield sublst


lst1 = [[1, 2], 3, 4, [5, 6], [7, 8, 9]]
print(list(generate1(lst1)))  # 使用内置函数list()将生成器转换为列表，显示输出结果为：[1, 2, 3, 4, 5, 6, 7, 8, 9]


# 使用递归实现取出多层嵌套列表元素
def generate2(lst2):
    for sublst in lst2:
        try:
            for num in generate2(sublst):
                yield num
        except:
            yield sublst


lst2 = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]]]
print(list(generate2(lst2)))
