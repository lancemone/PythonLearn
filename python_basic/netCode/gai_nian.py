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
