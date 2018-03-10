# 递归（Recursion）就是函数自己调用自己

# 无穷递归 （Infinite Recursion）
def recursion():
    return recursion()


recursion()  # 代码运行后会抛出异常，RecursionError: maximum recursion depth exceeded。意思是，递归错误：超过最大递归深度


# 阶乘运算
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i

    return result


print(factorial(5))


# 使用递归实现阶乘
def factorial1(n):
    print(n)
    if n == 1:
        return 1
    else:
        i = n * factorial1(n - 1)  # 函数中调用函数自身
        print(i)
        return


print(factorial1(5))


# 幂运算
def power(x, y):  # 定义函数计算参数的x的y次幂

    if y == 0:
        return 1
    else:
        result = 1
        for i in range(y):
            result *= x
        return result


print(power(2, 4))


# 使用递归函数幂运算
def power_recusion(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * power_recusion(x, y - 1)


print(power_recusion(2, 5))


# 二分查询
def search(seq, number, lower, upper):  # 定义函数,参数seq为要查询的序列,参数number为要查询的数字
    # 参数lower为查找区间的下限值,参数upper为查找区间的上限值
    if lower == upper:  # 查找区间仅剩一个数字时，即找到查询结果，停止循环调用
        assert number != seq[upper], '这里有问题！'  # 如果不相等会抛出异常AssertionError（断言错误）,可以尝试把"=="改为"!="
        print(str(lower))  # 显示输出结果为：66
    else:  # 查找区间有多个数字时，继续查找
        middle = (lower + upper) // 2  # 通过整除计算，获取查找区间数字的中间值
        if number > seq[middle]:  # 判断查找的数字是否大于中间值
            return search(seq, number, middle + 1, upper)  # 如果大于中间值，中间值作为查找区间下限值，继续查找
        else:
            return search(seq, number, lower, middle)  # 如果小于中间值，中间值作为查找区间上限值，继续查找


search(range(0, 100), 66, 0, 100)  # 显示输出结果为：66
