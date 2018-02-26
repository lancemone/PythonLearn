# 获取随机数，需要使用随机数的函数

# 随机数函数不能够直接使用，因为它不是内建函数，它存在于其它模块中.创建的Python文件（.py）就是模块（Module）

# 函数random()，能够随机获取一个18位0~1之间的小数
# 函数randrange(start,stop,step)，能够随机获取一个指定区间的正整数；参数start表示随机区间的起始数；参数stop表示随机区间的终止数，终止数不会被获取；参数step表示步长（数量），步长之间的部分不会被获取
import random

print(random.random())  # 调用模块中的函数random()，显示输出结果为一个18位0~1之间的随机小数。
print(random.randrange(10))  # 调用模块中的函数randfange()，显示输出结果为一个0~9之间的随机整数。
print(random.randrange(3, 21))  # 调用模块中的函数randfange()，显示输出结果为一个3~20之间的随机数。
print(random.randrange(0, 11, 2))  # 调用模块中的函数randfange()，显示输出结果为一个0~10之间的随机偶数。

# 只使用其中的randrange函数的话，我们不需要导入random模块，而是从random模块导入randrange这个函数
from random import randrange  # 从 random模块 导入 randrange函数

print(randrange(10))  # 调用模块中的函数randfange()，显示输出结果为一个0~9之间的随机整数。
print(randrange(3, 21))  # 调用模块中的函数randfange()，显示输出结果为一个3~20之间的随机数。
print(randrange(0, 11, 2))  # 调用模块中的函数randfange()，显示输出结果为一个0~10之间的随机偶数。
