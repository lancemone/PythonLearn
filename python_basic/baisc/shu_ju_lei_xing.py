# Python中有六种标准数据类型，分别为Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Set（集合）和Dict（字典）


# 数字类型包含：Int（整数）、Float（浮点数）、Bool（布尔）和Complex（复数）
# 整型（Int）：即整数，可以通过int(x[,base=10])函数将非整数或整数组成的字符串以及字节转换成整数。
print(int())  # 显示输出结果为0
print(int(1.23))  # 显示输出结果为1
print(int('5'))  # 显示输出结果为5
print(int('0xF', 16))  # 显示输出结果为15

# 浮点型（Float）：即小数，float([x])函数将非整数或整数组成的字符串以及字节转换成整数。
print(float())  # 显示输出结果为0.0
print(float(1))  # 显示输出结果为1.0
print(float('5'))  # 显示输出结果为5.0
print(float(0xf))  # 显示输出结果为15.0

# 布尔类型（Bool）：通过bool(x)函数，能够得到参数x的布尔值。
# 在Python中除了空值、”、False、0、()、[]、{}、None为False，其它均为True。
print(bool())  # 显示输出结果为False
print(bool(False))  # 显示输出结果为False
print(bool(''))  # 显示输出结果为False
print(bool(0))  # 显示输出结果为False
print(bool(None))  # 显示输出结果为False
print(bool([]))  # 显示输出结果为False
print(bool(()))  # 显示输出结果为False
print(bool({}))  # 显示输出结果为False

# 复数（Complex）：能够通过complex(x)函数创建一个复数。
print(complex(1))  # 显示输出结果为：(1+0j)
print(complex('2+1j'))  # 显示输出结果为：(2+1j)
print(complex(2, 5))  # 显示输出结果为：(2+5j)

# 字符串（String）：通过str(object=”)函数能够将对象转换为字符串。

# 迭代对象合并为字符串。join(iterable)函数能够将可迭代对象的元素或多个字符串合并为一个字符串，参数iterable为可迭代对象。如果参数不是字符串会抛出类型错误的异常，包括字节对象。
lst1 = '1', '2', '3'
print('+'.join(lst1))  # 显示输出结果为：1+2+3
print(''.join(lst1))  # 显示输出结果为：123

# 字符串内单词首字母大写
# 使用string模块中的capwords(s[,sep])函数，参数s为需要转换的字符串，参数sep为分隔符，省略参数sep时，每个单词均转换为首字母大写单词； \
# 未省略参数sep时，除了第一个单词首字母转换为大写，分隔符后方的第一个字母均转换为大写。
import string

old_str = 'my name is lance mone'
new_str1 = string.capwords(old_str)
new_str2 = string.capwords(old_str, 's ')
print(new_str1, new_str2)

# 多字符转换。使用字符串对象调用translate(table)函数，参数table为转换表；使用这个函数我们需要先创建转换表，转换表包含256个 ASCII字符。
# 可以使用关键字str调用maketrans(x[,y[,z]])函数创建转换表
table1 = str.maketrans({111: '*'})  # 只有1个参数时，必须输入一个字典，字典的键值可以是ASCII字符或对应的数字序号，转换时会用值对应的字符替换键对应的字符
print('photo'.translate(table1))  # 显示输出结果为：ph*t*

table2 = str.maketrans('o', '*')
print('photo'.translate(table2))  # # 显示输出结果为：ph*t*

table = str.maketrans('o', '*', 'po')  # 输入3个参数时，最后一个参数必须是字符串，包含在这个字符串中的每一个字符都被替换为None（空值）
print('photo'.translate(table))  # 显示输出结果为：ht
