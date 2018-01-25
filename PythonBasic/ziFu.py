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


