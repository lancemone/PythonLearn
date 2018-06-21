# IP地址是一个32位的二进制整数，按8位划分后，每一段都转换为十进制数
# TCP/IP全称是Transmission Control Protocol/Internet Protocol，中文译名为传输控制协议/因特网互联协议。
# IP协议负责传输数据，TCP协议负责控制传输的数据，所以IP协议是TCP协议的底层协议
# UDP协议全称是User Datagram Protocol，中文译名为用户数据报协议。仅仅将要发送的数据传送至网络，并接收网络传回的反馈，而不与接收端建立连接


# Socket(套接字)用于描述IP地址和端口
# 应用程序能够通过套接字向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
# 套接字包括两个：服务端套接字和客户端套接字
# 当我们创建一个服务端套接字之后，它就开始在网络地址中（服务器的IP地址+端口号）进行监听，随时处理来自客户端的连接。
# 因为来自客户端的连接可能是多个，所以处理服务端的套接字比处理客户端的套接字复杂。
# 处理客户端的套接字，只是建立连接，处理事务和关闭连接


# Socket 模块
# socket模块中的socket()函数，能够使用给定的地址族、套接字类型和协议号创建一个新的套接字
# 地址族：默认为socket.AF_INET，指定使用IPv4 网络协议；如果填入socket.AF_INET6，则能够使用IPv6 网络协议。
# 套接字类型：默认为socket.SOCK_STREAM，指定使用TCP协议的套接字流类型；如果填入socket.SOCK_DGRAM，则是使用UDP的套接字数据报类型。
# 协议号：默认为0
# 当创建了一个套接字，就需要使用bind()方法为其绑定主机地址和端口号，以便能够进行连接。还需要通过listen()方法，指定套接字最大等待连接数。当等待连接的数量超出最大限制数量时，后发起连接的客户端会被拒绝连接。
# 服务器与客户端的连接通过accept()方法完成，这个方法能够返回一个SSL（Secure Sockets Layer 安全套接层）通道和客户端的IP地址。
# 通过SSL通道，我们可以实现服务器和客户端的通信


import socket

# 创建服务端
skt = socket.socket()  # 创建套接字对象
host = '127.0.0.1'  # 指定主机IP地址
port = 4343  # 指定连接端口号
skt.bind((host, port))  # 为套接字对象绑定主机名称和端口号
skt.listen(3)  # 设置最大等待连接数
while True:
    print('waitting for connect...')
    ssl, addr = skt.accept()  # 获取服务端的SSL通道和远程客户端地址
    print('connect to:', addr)
    cname = ssl.recv(1024).decode()  # 获取客户端发来的信息，recv()方法的参数是一次读取的字节数量
    # ssl.send('Welcome come from {0}\'{1}'.format(addr, cname).encode())     # 通过SSL通道发送信息.send()方法参数为发送的数据
    ssl.send('Welcome come to my home')
    print('close connect...')
    ssl.close()  # 关闭SSL通道

# 创建客户端
skt_c = socket.socket()  # 创建套接字对象
host = '127.0.0.1'
port = 54059
skt_c.connect(('127.0.0.1', 4343))

print('receive message:', skt_c.recv(1024).decode())

import socket

# socketserver模块创建服务器
# socketserver模块的TCPServer类和UDPServer类分别针对TCP套接字流和UDP套接字数据报
# 使用socketserver模块创建一个服务器，我们需要创建一个对请求进行处理的类，继承StreamRequestHandler类，并重写请求处理方法handle()
# 当服务器接收到一个客户端连接发来的请求时，就实例化一个对请求进行处理的类，并调用实例中的请求处理方法进行处理。
'''当服务器与客户端进行通信时，我们可以使用以下方法：

self.request.recv()：接收客户端连接请求中发来的信息
self.rfile.readline()：读取客户端发来的信息
self.request.send()：向客户端连接请求发送信息（可能多次发送，直至完成）
self.request.sendall()：向客户端连接请求发送信息（一次全部发送）
self.wfile.write()：向客户端写入并发送信息.rfile和wfile是StreamRequestHandler类的两个属性，通过这两个属性能够进行写入与读取，所以通过这两个类文件对象（file-like Object）就能够实现服务器和客户端的通信。
Python中的类文件对象（file-like object）是指实现了read()方法或write()的对象
根据创建的方式，一个文件对象可以是一个真正的磁盘文件，也可以是对存储或通信设备的访问（例如标准输入/输出、内存缓冲区、套接字、管道等）。所以，文件对象也可称为类文件对象或流。
'''

# 创建服务端
from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):  # 定义类继承对数据流请求处理类
    def handle(self):  # 定义处理方法
        addr = self.client_address  # 获取客户端地址
        print('处理来自%s的连接' % (addr))
        cname = self.request.recv(1024).decode()  # 获取客户端发来的信息
        # cname = self.rfile.readline().decode()
        self.request.sendall('欢迎来自{0}的{1}'.format(addr, cname).encode())  # 向客户端发送信息
        # self.request.send('欢迎来自{0}的{1}'.format(addr, cname).encode())  # 向客户端发送信息
        # self.wfile.write('欢迎来自{0}的{1}'.format(addr, cname).encode()) # 向客户端发送信息


server = TCPServer(('', 6666), Handler)  # 实例化TCP服务器
server.serve_forever()  # 持久运行服务器

# 异步网络编程：使用多线程实现多连接处理
# 创建一个新的服务器类，继承ThreadingMixIn类和 TCPServer类
from socketserver import TCPServer, StreamRequestHandler, ThreadingMixIn
import threading


class Server(ThreadingMixIn, TCPServer):  # 创建服务器类（注意继承顺序）
    pass  # 无需添加代码


class Handlerr(StreamRequestHandler):
    def handlee(self):
        addr = self.client_address
        print('线程%s处理来自%s的连接...' % (threading.current_thread().name, addr))
        cname = self.request.recv(1024).decode()
        self.request.sendall('欢迎来自{0}的{1}'.format(addr, cname).encode())


serverr = Server(('', 6666), Handlerr)
serverr.serve_forever()

# select模块：使用select模块来实现多连接并发的处理
"""
实现下述功能：

客户端向服务器发送需要翻译的汉字，服务器端将相应的翻译结果（英文单词）发送回客户端。
如果没有相应的翻译结果，服务器端发回信息：未找到对应的英文单词！
如果客户端未发送的信息为空值或“exit”，能够关闭服务器。

"""
# 客户端
s = socket.socket()
host = socket.gethostname()
port = 6677
s.connect((host, port))  # 向服务器请求连接
while True:
    char = input('输入中文：')  # 获取用户输入
    s.send(char.encode())  # 编码后发送到服务器
    if char in ['exit', '']:  # 如果发送的内容为‘exit’或空值
        break  # 跳出循环，结束程序
    print('英文单词：', s.recv(1024).decode())  # 显示输出来自服务端的信息

# 服务端
import socket, select


def translate(char):
    my_dict = {'你': 'you', '我': 'me', '他': 'he'}  # 定义可翻译的内容
    if char not in my_dict:
        return 'Donot find this word'
    else:
        return my_dict[char]


s = socket.socket()  # 创建套接字
host = socket.gethostname()
port = 5678
s.bind((host, port))
s.listen(5)

# 通过select模块实现异步I/O
'''
select.select(rlist, wlist, xlist[, timeout])函数
这个函数的三个必填参数均为序列，序列中为“等待的对象”，可选参数为数字：

rlist：一个列表，包含等待直到能够读取的对象；可以为空列表。
wlist：一个列表，包含等待直到能够写入的对象；可以为空列表。
xlist：一个列表，包含等待出现一个“异常状态”的对象；可以为空列表。
timeout：连接超时的时长，值为秒的浮点数；省略此参数时，函数将阻塞，直到至少一个“等待的对象”准备好；如果参数为0，则从不阻塞。

函数的返回值是一个元组，包含3个已经准备好的对象的列表，当没有准备好的对象或连接超时，则返回3个空列表。

'''

inputs = [s]  # 创建等待能够读取对象的列表，默认包含等待连接的套接字。
while True:
    print('等待连接...')
    rs, ws, xs = select.select(inputs, [], [])  # 获取已经准备好的对象列表
    for r in rs:  # 遍历已经准备好的可读取对象列表
        if r is s:  # 如果列表元素是套接字对象
            ssl, addr = r.accept()  # 等待客户端连接
            print('连接到：', addr)
            print(type(ssl))
            inputs.append(ssl)  # 连接成功后，将SSL通道对象添加到等待可读对象列表
        else:  # 否则(对象是SSL通道)
            try:
                char = r.recv(1024).decode()  # 通过SSL通道接收来自客户端的信息
                if char in ['', 'exit']:  # 判断信息内容是否空值或“exit”
                    print(addr, '主动关闭连接！')
                    inputs.remove(r)  # 从等待可读取对象的列表中移除SSL通道对象
                else:  # 否则
                    r.send(translate(char).encode())  # 通过SSL通道向客户端发送翻译结果
                    print('完成任务...')
            except:  # 捕获连接出现的异常
                print(addr, '异常断开连接！')
                inputs.remove(r)  # 从等待可读取对象的列表中移除SSL通道对象
