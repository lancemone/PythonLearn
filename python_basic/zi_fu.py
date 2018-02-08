#打印语句，输出HELLO WORLD
print("Hello World")
#字符串中引号的使用
#单引号
print('this is python')
#双引号
print("this' python")
#三引号
print('''this' is my "little cute" and gf''')
#自然字符串（指示某些不需要特别处理的字符串，如转义符等）
print(r"Newlines are indicated by\n")
#转义符\       http://www.opython.com/143.html
print("Newlines are indicated by\
n")
#转义符转义''或“”
print('i\'m \"ok \"!')
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('i\'m learning python \ni\'m so happy')
print('\\\n\\')
print('\\\t\\')
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''
line1
line2
line3''')
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')
print(r'''hello,\n 
world''')
print(r"hello \n'\tworld'")


#Unicode字符串
print('你好=مرحب')
#按字面意义连级字符串
print('What\'s' ' your name?')
#使用变量和字面意义上的常量
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'), ord('中'))
#chr()函数把编码转换为对应的字符
print(chr(66), chr(25991))

#计算str包含多少个字符，可以用len()函数
print(len(b'abc'), len('中文'), len('中文'.encode('utf-8')))

#格式化字符串  输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串
#用 % 实现格式化，在字符串内部，%s表示用字符串替换，%d表示用整数替换，%f表示浮点数替换，%x表示十六进制数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
print('hello, %s' % 'world')    #输出结果 hello, world
print('目前%s仅占到全国总人口的%d%%' % ('大学生', 6))   #用%%来表示一个%
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))    #输出结果：3-01
print('%.2f' % 3.1415926)     #输出结果：3.14
'''
name = input('请输入学生姓名：')
s1 = int(input('请输入期中成绩：'))
s2 = int(input('请输入期末成绩：'))

if s2 > s1:
    r = (s2 - s1) / s1 * 100
    print('%s分数提升了%.1f%%' % (name, r))
else:
    r = (s1 - s2) / s1 * 100
    print('%s分数下降了%.1f%%' % (name, r))      '''


#获取字符串长度
long = len('这个字符串有多长我也不知道')
print(long)
#当我们对中文进行编码，采用“UTF-8”编码类型时，一个汉字的字节数量是3
long1 = len('这个字符串有多长我也不知道'.encode('utf-8'))
print(long1)


#截取字符串，对字符串进行切片操作
#切片操作是将字符串赋值到一个变量，然后通过输入截取的起始位置、终止位置以及方向与间隔，对字符串进行不同方式的截取
#例如：str[3:9:2] 这段代码表示对“str”这个变量中的字符串进行切片操作，“3”表示切片的起始位置为第4个字符（字符串中字符的索引位置从0开始），“9”表示切片的终止位置（终止位置不会被截取），“2”表示从左向右每隔1位进行截取（负数表示从右至左截取）
str = '123456789'

print (str[:]) # 截取全部字符
print (str[2]) # 截取第3位字符
print (str[:3]) # 截取第1位到第4位之前的字符
print (str[2:5]) # 截取第3位到第6位之前的字符
print (str[5:]) # 截取第6个字符到末尾的字符
print (str[5::3]) # 从第6个字符开始每隔2个字符截取到末尾的字符
print (str[-1]) # 截取倒数第一个字符
print (str[:-3]) # 截取第1位到倒数第3位之前的字符
print (str[-3:-1]) # 截取倒数第3位到倒数第1位之前的字符
print (str[-3:]) # 截取倒数第3位到末尾的字符
print (str[::-1]) # 倒序截取全部字符
print (str[::-2]) # 倒序从倒数第1位开始每间隔1个字符截取字符
print (str[5::-1]) # 倒序截取第6位到开始的字符
print (str[5:2:-1]) # 倒序截取第6位到第3位之后的字符
print (str[:-6:-1]) # 倒序截取末尾到倒数第6位之后的字符
print (str[-1:-6:-1]) # 倒序截取末尾到倒数第6位之后的字符
print (str[-2:-8:-2]) # 倒序从倒数第2位开始间隔1位截取到倒数第8位之后的字符


#重复字符串
print('hello \n' *9)

#字符串大小写转换
'''
大小写转换的方法有以下几种：

upper()： 字符串全部字符转换为大写
lower()：字符串全部字符转换为小写
swapcase() ：字符串全部字符大小写互换
capitalize()：字符串首个单词首字母大写
title()： 字符串中全部单词首字母大写
这些方法均不用写入参数，直接调用       '''

s = "i'm a SuperMan"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

#替换部分字符   替换部分字符的方法是“replace(old,new,count)”
'''old：表示需要被替换的字符或字符串；
new：表示替换后的新字符或字符串；
count：表示替换的次数，此参数可省略；如果省略表示替换所有需要被替换的字符或字符串。   '''

s = "i'm a good boy and i'm so happy i can meet her"
print(s.replace('i\'m', 'you\'re'))    #you're a good boy and you're so happy i can meet her
print(s.replace('i\'m', 'you\'re', 1))   #you're a good boy and i'm so happy i can meet her


#去除字符串两侧指定内容
'''字符串去除两侧指定内容的方法有三种：
strip(chars) ：去除字符串两侧的指定内容，并且，可以同时去除多个相同的指定内容；参数chars为指定的一个或多个字符，不填入该参数则去除字符串两侧所有空格。
lstrip(chars)  ：去除字符串左侧的指定内容，并且，可以同时去除多个相同的指定内容；参数chars为指定的一个或多个字符，不填入该参数则去除字符串左侧所有空格。
rstrip(chars) ：去除字符串右侧的指定内容，并且，可以同时去除多个相同的指定内容；参数chars为指定的一个或多个字符，不填入该参数则去除字符串右侧所有空格。'''

str1 = '   人人为我 我为人人   '
str2 = '人人为我 我为人人'

print (str1)
print (str1.strip())
print (str1.lstrip())
print (str1.rstrip())
print (str2.strip('人'))
print (str2.lstrip('人'))
print (str2.rstrip('人'))
print (str2.strip('人人为'))


#字符串查询
'''字符串查询的方法有两种：

第一种：index(sub,start,end)和rindex(sub,start,end)

index方法是从左至右查询，rindex方法是从右至左查询；

参数sub是指被查询的字符或字符串，参数start是查询的起始位置，参数end是查询的终止位置（终止位置不在查询范围内）；

参数start和参数end可以同时省略，这时为查询字符串中全部字符；也可以只省略参数end，表示查询范围为起始位置至末尾。   '''

s = '人人为我，我为人人。'

print (s.index('人')) # 从左向右查询全部字符     0
print (s.index('人',2)) # 从左侧第3个字符开始向右查询至末尾     7
print (s.rindex('人')) # 从右向左查询全部字符      8
print (s.rindex('人',0,8)) # 从右侧第9个字符之前向左查询至首位      7

'''第二种：find(sub,start,end)和rfind(sub,start,end)

这两个函数和index函数以及rindex函数作用相同，并且用法相同。

但是，当没有查询结果时，index函数与rindex函数会提示错误：ValueError：substring not find（值错误：未发现被查询的字符串）。

而另外的两个函数，find函数和rfind函数，在没有查询结果时，返回值为-1'''

s = '人人为我，我为人人。'

print (s.find('地'))
print (s.index('地'))


#字符串中字符的计数
'''字符串的计数方法是count(x,start,end)，这个函数可以统计字符串中被查询的字符或字符串出现的次数。

参数x是指被查询的字符或字符串，参数start是查询的起始位置，参数end是查询的终止位置（终止位置不在查询范围内）；

参数start和参数end可以同时省略，这时为查询字符串中全部字符；也可以只省略参数end，表示查询范围为起始位置至末尾。'''

s = '人人为我，我为人人。'

print(s.count('人'))  # 计算字符串中被查询字符或字符串出现的次数
print(s.count('人人'))  # 计算字符串中被查询字符或字符串出现的次数
print(s.count('人', 0, 8))  # 计算从字符串首位到第9个字符（不含第9个字符）之间被查询字符或字符串出现的次数
