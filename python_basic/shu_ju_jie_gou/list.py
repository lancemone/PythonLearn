# 形式上列表和元组的区别只在于列表两侧是方括号

lst11 = []  # 创建空的列表
lst22 = [1]
lst33 = [1, 2, 3, 4]
classmates = ['fangfang', '明明', '方刚']
print(lst11, lst22, lst33, classmates)

# 列表元素是可变的，因此列表操作比元组更为丰富。
# 除了和元组相同的操作之外，列表还有其他的操作，例如添加、插入、取出、删除以及修改列表所包含的元素
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 创建列表
lst2 = ['a', 'b', 'c']
lst3 = ['你', '我', '你', '他', '我', '我']

print(len(lst1))  # 获取列表的元素数量
print(lst1 + lst2)  # 连接多个列表为一个新列表
print(lst2 * 3)  # 重复列表元素为一个新列表
print(lst1[0])  # 获取列表指定位置的元素，索引位置从左至右由0开始
print(lst1[-1])  # 获取列表指定位置的元素，索引位置从右至左由-1开始
print(lst1[2:8:2])  # 获取列表中指定片段的元素，并可以设置间隔获取
print(max(lst1))  # 数组中元素均为数字类型时，获取列表中数值最大的元素
print(min(lst1))  # 数组中元素均为数字类型时，获取列表中数值最小的元素
print('a' in lst1)  # 判断列表中是否包含某个元素，如果包含，返回值为True，否则为False
print(lst1.index(3))  # 查询元组中是否包含某个元素，如果包含，返回值为索引位置，否则抛出异常
print(lst3.count('我'))  # 获取元组中某个元素的出现次数

# 添加元素

lst11.append(1)  # 添加单个元素到列表。append(object)函数可以为列表添加单个元素，参数object为对象；
lst33.extend(6, 7, 8)  # 添加多个元素到列表，使用extend(iterable)函数可以为列表添加多个元素，参数iterable为可迭代对象。
print(lst11, lst33)

# 更改元素
lst33[0] = 'one'  # 列表[索引位置] = 新元素
# 更改多个元素：列表[起始位置,终止位置] = 新元素
lst33[2:6] = 'three', 'four'  # 更改指定位置区间的元素为新元素，数量无需对应

# 插入元素
# 插入单个元素：使用insert(index,object)函数，参数index为索引位置，表示在该位置之前插入新的元素；参数object为对象
lst33.insert(0, '排序')  # 起始位置插入元素
# 插入多个元素：列表[索引位置:索引位置] = 新元素；注意，两个索引位置保持一致。
lst33[3:3] = '3', '2', '1'  # 指定位置前方插入新元素

# 取出元素    使用pop(index)函数，参数index为被取出元素的索引位置。

print(lst33.pop(4))

# 删除元素
# 删除指定内容元素：使用remove(object)函数可以删除列表中首次出现的与参数相同的元素，如果列表中不存在与参数相同的元素则抛出异常
lst33.remove(2)
# 删除单个指定位置元素： del列表[索引位置]
del lst33[1]
# 删除多个指定位置元素： del列表[起始位置:终止位置]
del lst33[2:4]
# 删除末尾元素：使用pop()函数，参数为空即可。
lst33.pop()
# 清空所有元素:clear()函数或者del命令：del列表[:]
lst33.clear()
del lst11[:]

# 列表排序

lst01 = [3, 1, 5, 7, 6, 9]
lst01.reverse()  # 反向排序：使用reverse()函数
# 升降排序：使用sort(cmp,key，reverse)函数，参数cmp为函数，参数key为函数，reverse为布尔值（True和False）
lst01.sort()  # 参数为空时默认为升序排列
lst01.sort(reverse=True)  # 通过设置参数reverse=True，转换为降序排列
# 升降序排列也可以使用函数sorted(iterable,cmp，key，reverse)，参数iterable为可迭代对象；参数cmp为函数，参数key为函数，reverse为布尔值
# sorted()函数不会改变原列表
