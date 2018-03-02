def spam(a, b=[]):
    print(b)
    return b


x = spam(1)
x.append(99)
print(x)
spam(1)
