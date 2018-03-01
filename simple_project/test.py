def avg(first, *rest):  # 使用一个*参数让一个函数接受任意数量的位置参数
    return (first + sum(rest)) / (1 + len(rest))  # rest是由所有其他位置参数组成的元组。然后我们在代码中把它当成了一个序列来进行后续的计算。


print(avg(1, 2))  # 1.5
print(avg(1, 2, 3, 4))  # 2.5
