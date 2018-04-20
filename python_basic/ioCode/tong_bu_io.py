# 同步IO


# 文件读写：读写文件是最常见的IO操作。
# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，\
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
# 读文件
try:
    f = open('/Users/taomo/Documents/Chrome.txt', 'r')  # 标示符'r'表示读
    # 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
    print(f.read())
    # 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
finally:
    if f:
        f.close()  # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
with open('/Users/taomo/Documents/Chrome.txt', 'r') as f:
    print(f.read())

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
for line in f.readlines():
    print(line.strip())

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 读取二进制文件：要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
rb = open('/Users/taomo/Downloads/63471797_p0_master1200.jpg', 'rb')
print(rb.read())  # 输出十六进制表示的字节
# 字符编码：要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
gbk = open('/Users/taomo/Downloads/gbk.gbk', 'r', encoding='gbk')
print(gbk.read())

# 写文件：写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('/Users/taomo/Downloads/wenben.txt', 'w')as w:
    w.write('hi girls')

# StringIO 在内存中读写str
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO

str1 = StringIO()
print(str1.write('hello'))  # 输出 5
print(str1.getvalue())  # 输出 hello getvalue()方法用于获得写入后的str

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
str2 = StringIO('hello')
while True:
    s = str2.read()
    if s == '':
        break
    print(s.strip())

# BytesIO StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO

by = BytesIO()
print(by.write('中文'.encode('utf-8')))  # 输出 6
print(by.getvalue())  # 输出十六进制字符串

# 操作文件和目录 要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
# Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os

print(os.name)  # 获取操作系统类型.如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.uname())  # 获取系统的详细信息
print(os.environ)  # 获取操作系统中定义的环境变量
print(os.environ.get('PATH'))  # 获取操作系统中定义的环境变量的某个值调用os.environ.get('key')

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
