lst01 = [3, 1, 5, 7, 6, 9]
lst01.reverse()  # 反向排序：使用reverse()函数
print(lst01)
# 升降排序：使用sort(cmp,key，reverse)函数，参数cmp为函数，参数key为函数，reverse为布尔值（True和False）
lst01.sort()  # 参数为空时默认为升序排列
lst01.sort(reverse=True)  # 通过设置参数reverse=True，转换为降序排列
# 升降序排列也可以使用函数sorted(iterable,cmp，key，reverse)，参数iterable为可迭代对象；参数cmp为函数，参数key为函数，reverse为布尔值
# sorted()函数不会改变原列表
print(sorted(lst01))  # 输出显示升序列表
print(sorted(lst01, reverse=True))  # 输出显示降序列表
print(lst01)  # 输出显示原列表
