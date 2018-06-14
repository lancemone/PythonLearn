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
