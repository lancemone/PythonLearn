def factorial1(n):
    print(n)
    if n == 1:
        return 1
    else:
        i = n * factorial1(n - 1)
        print(i)
    return i  # 函数中调用函数自身


print(factorial1(5))
