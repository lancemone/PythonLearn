# 字典 dict
# 字典同样是一个序列，不过字典的元素是由key（键，可理解为关键字或名称）与values（值）组成
# 字典中的值没有特定顺序，但必须用一个特定的键存储。字典的键必须是不可变的数据类型，可以是数字、字符串或者元组。
# 这种能够通过名称引用值的数据类型称做映射（Mapping），字典是Python中唯一内建的映射类型。
# 字典中不能够出现相同的键，但可以出现相同的值;字典中的键不能够更改，但值可以更改;字典的值可以为Python中的任何对象。


# 创建字典： 创建字典可以直接按格式创建，也可以使用dict()方法进行创建。
# dict(**kwarg)：参数**kwarg为可变关键字参数；dict(mapping, **kwarg)：参数mapping为映射函数；dict(iterable, **kwarg)：参数iterable为可迭代对象。

d0 = {}  # 创建空字典
d1 = dict()  # dict()方法创建空字典
d2 = {'yue': ['月', '约', '悦'], 'ri': '日', 'yi': 1}  # 创建字典
d3 = dict(小楼='xiaolou', 小美='beautiful')  # 通过可变参数创建对象
d4 = dict([1, 2, 3, 4], [(5, 6, 7), (8, 9)])  # 通过可迭代对象（列表）创建字典

# 还有一种字典的创建方式，通过fromkeys(seq,value)方法进行创建，参数seq为包含key的序列，参数value为key的默认值。
k = ['小楼', '明步']  # key的列表
d5 = dict.fromkeys(k)  # 从key的列表创建字典
d6 = dict.fromkeys(k, '哦哦')  # 从key的列表创建字典，并赋予默认值
print(d1)  # 显示输出结果为：{'小楼': None, '明步': None}
print(d2)  # 显示输出结果为：{'小楼': '哦哦', '明步': '哦哦'}

# 查询元素：我们可以使用items()方法，通过items()方法可以获取到字典中所有元素的迭代器
print(d2.keys())  # 可以使用keys()方法获取到字典中所有元素键的迭代器
# 查询元素值有多种方法：
print(d2['yue'])  # 通过键可以获取相对应的值：字典[键]
print(d2.get('yue', 404))  # 通过get(k,default)方法查询，参数k为查询的键，参数default为未查询到结果时的默认值。例：print(d2.get('aaa', 404))
print(d2.values())  # 通过values()方法获取到字典中所有元素值的迭代器

# 添加元素
# 通过“字典[键]=值”的方式进行添加，如果字典中不存在相同的键则自动添加，否则修改已存在的键所对应的值。
d3['小明'] = 'xiaoming'  # 添加新元素到字典
print(d3)
d3['小楼'] = 'xiaol'  # 修改已存在键对应值
print(d3)
d3['小樱'] = 'xiao', 'ying'  # 添加值为元组的新元素到字典
print(d3)
# 通过setdefault(k,default)方法进行添加，参数k为指定的键，参数default为默认值。当字典中存在指定的键时，能够返回该键所对应的值；如果不存在指定的键时，则会返回参数default中设置的值，同时，在字典中会添加新元素，新元素的键即为参数k，值即为参数default。
print(d3.setdefault('小楼', 'xiaolou'))  # 字典中存在相应的键，则返回该键对应的值    输出结果： xiaol
print(d3.setdefault('小井', 'xiaojing'))  # 字典中不存在相应的键，则返回default参数的值    输出结果：xiaojing
# 添加多个元素：通过update(m,kwargs)方法进行添加，参数m（mapping）为映射函数，kwargs为可变参数
d3.update(樱井='yingjing', 明步='mingbu')  # 通过可变参数添加多个元素
print(d3)
d3.update((('樱井', '好白'), ('明步', '好大')))  # 通过元组添加多个元素
print(d3)
d3.update([('樱井', '好白'), ('明步', '好大')])  # 通过列表添加多个元素
print(d3)
d3.update({'樱井': '好白', '明步': '好大'})  # 通过字典添加多个元素
print(d3)
d3.update(d2)  # 合并字典元素
print(d3)

# 删除元素 使用del指令可以通过键删除某个元素：del 字典[键]
del d3['樱井']  # 删除元素
print(d3)

# 取出元素与元素值   使用popitem()方法在字典中取出元素
print(d3.popitem())  # 取出末尾的元素与元素值
print(d3)
# 使用pop(k,default)方法在字典中取出指定元素的值，参数k为指定元素的键，参数default为未取到结果时的默认值。
print(d3)
print(d3.pop('小楼'))
print(d3.pop('樱井', '好爽'))  # 显示输出结果为：好爽
print(d3)

# 设置默认值
print(d3.setdefault('小楼', '好棒'))  # 显示输出结果为：好帅
print(d3.setdefault('樱井', '好爽'))  # 显示输出结果为：好爽
print(d3)

'''字典也支持使用以下方法：

clear()：清空字典

copy()：复制字典：

len()：获取字典元素数量

max()：获取字典中最大的键

min()：获取字典中最小的键

同时，字典也支持通过in和not in进行成员关系的判断。'''
