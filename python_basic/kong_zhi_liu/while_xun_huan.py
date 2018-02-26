# 循环显示输出列表内容
ll = ['H', 'E', 'L', 'L', 'O']  # 创建列表
n = 0  # 创建变量，用于计数
while n < len(ll):  # 循环，条件为计数数量小于列表元素数量
    print(ll[n], end='')  # 符合条件时，将计数数量作为列表索引，获取元素显示输出
    n += 1  # 计数数量自增1
#  重复显示输出
n = 0  # 创建变量，用于计数
while n < 5:  # 循环，条件为计数数量小于重复次数
    print(ll)  # 符合条件时，显示输出字符串内容
    n += 1  # 计数数量自增1


# 1、斐波那契数列子序列程序
a, b = 0, 1
while b < 10:
    print(b)     #用一个逗号结尾可以禁止换行输出 print(b, end=',')
    a, b = b, a+b

# 2、while循环中加入if判断
num = 23

guess = int(input('Enter your guess number :'))

while guess != num:
    if guess > num:
        print('No, it is a little lower than that')
        guess = int(input('Enter your guess number :'))
    else:
        print('No, it is a little higher than that')
        guess = int(input('Enter your guess number :'))
print('Done')

