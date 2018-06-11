import socket

skt_c = socket.socket()  # 创建套接字对象
host = '127.0.0.1'
port = 54059
skt_c.connect(('127.0.0.1', 4343))

print('receive message:', skt_c.recv(1024).decode())
