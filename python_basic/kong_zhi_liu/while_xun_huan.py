
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

