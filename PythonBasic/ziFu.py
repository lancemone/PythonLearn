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
#转义符\
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


