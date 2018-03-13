# 列表推导式（List Comprehension）：一种采用简洁的方式来处理序列中的全部或部分元素，并返回结果列表。
lst1 = [x * x for x in range(1, 7)]  # 列表推导式：循环获取范围1~6的整数，计算乘积后添加到新列表。
print(lst1)  # 显示输出结果为：[1, 4, 9, 16, 25, 36]

# 列表推导式设置条件
lst2 = [x * x for x in range(1, 7) if x % 2 == 0]
print(lst2)  # 显示输出结果为：[4, 16, 36]

# 列表推导式的组成为：[元素(或计算方法) for循环(允许多个) if语句]
# 在列表推导式中有多个循环时，会出现嵌套循环的效果，而不是同步循环的效果

# 错误代码示例（从整数列表中取出小于3的元素，并从平方列表中取出对应的元素，组成算式列表。）
# 也就是说，当前面的循环取出第1个元素，后方的循环会进行一轮迭代；当前面的循环取出第2个元素，后方的循环又会进行一轮迭代；以此类推，直到前方的循环完成一轮迭代为止。
number = [1, 2, 3, 4, 5, 6]
square = [1, 4, 9, 16, 25, 36]
lst3 = ['{0}² = {1}'.format(str(x), str(y)) for x in number for y in square if x <= 3]
print(lst3)

# 正确代码  需要增加条件，当前方循环取出元素的平方等于后方循环取出元素的时候，再添加到列表
lst4 = ['{0}² = {1}'.format(str(x), str(y)) for x in number for y in square if x <= 3 and x * x == y]
print(lst4)

# 上方代码等同于
lst = []  # 此部分用列表推导式替代
for x in number:  # 此部分用列表推导式替代
    for y in square:  # 此部分用列表推导式替代
        if x <= 3 and x * x == y:  # 此部分用列表推导式替代
            lst.append('{0}²={1}'.format(str(x), str(y)))  # 此部分用列表推导式替代
print(lst)

# lambda 表达式：一个匿名内联函数，由一个表达式组成，在函数被调用时求值
# 创建lambda函数的语法： lambda [参数] : 表达式
# 尽管lambda表达式允许你定义简单函数，但是它的使用是有限制的。 你只能指定单个表达式，它的值就是最后的返回值。也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等。
add = lambda x, y: x + y
print(add(3, 4))

# lambda表达式的典型使用场景是排序和数据reduce等
names = ['david', 'raymond', 'ned', 'batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))  # 按首字母排序

numbers = [1, 2, 3, 4, 5, 6]
lst11 = list(filter(lambda x: x % 2 == 0, numbers))  # 通过lambda表达式对每个number的元素进行验证，并将所有验证结果转换为list。
print(lst11)

# 匿名函数捕获变量值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))
# 上面两个返回结果都是30，lambda表达式中的x是一个自由变量，在运行时绑定值，而不是在定义时绑定值。和函数的默认参数定义不同，x的值是执行时的值
x = 10
a = lambda y: x + y
print(a(10))
x = 20
b = lambda y: x + y
print(b(10))

# 使匿名函数在定义时就捕获值，将参数值定义成默认参数即可
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))

# 通过在一个循环或列表推导中创建一个lambda表达式列表，并在定义时就记住每次的迭代值。
funces = [lambda x, n=n: x + n for n in range(5)]
for f in funces:
    print(f(0))

# 从姓名集合中筛选出姓氏为“李”的姓名
name_set = {'邢佳栋', '李学庆', '高昊', '潘粤明', '戴军', '薛之谦', '贾宏声', '于波', '李连杰', \
            '王斑', '蓝雨', '刘恩佑', '任泉', '李光洁', '姜文', '黑龙', '张殿菲', '邓超', '张杰', \
            '杨坤', '沙溢', '李茂', '黄磊', '于小伟', '刘冠翔', '秦俊杰', '张琳', '陈坤', '黄觉', \
            '邵峰', '陈旭', '马天宇', '杨子', '邓安奇', '赵鸿飞', '马可', '黄海波', '黄志忠', '李晨', \
            '后弦', '王挺', '何炅', '朱亚文', '胡军', '许亚军', '张涵予', '贾乃亮', '陆虎', '印小天', \
            '于和伟', '田亮', '夏雨', '李亚鹏', '胡兵', '王睿', '保剑锋', '于震', '苏醒', '胡夏', '张丰毅', \
            '刘翔', '李玉刚', '林依轮', '袁弘', '朱雨辰', '丁志诚', '黄征', '张子健', '许嵩'}
lst01 = list(x for x in name_set if '李' in x[0])  # 使用列表推导式获取新列表
lst02 = list(filter(lambda x: x[0] == '李', name_set))  # 使用匿名函数
print(lst01)
print(lst02)
