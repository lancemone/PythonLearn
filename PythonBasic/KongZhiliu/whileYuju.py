
# 1、斐波那契数列子序列程序
a, b = 0, 1
while b < 10:
    print(b)     #用一个逗号结尾可以禁止换行输出 print(b, end=',')
    a, b = b, a+b


