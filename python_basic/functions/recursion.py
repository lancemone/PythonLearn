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
