import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',1234))
print(sock.recv(100).decode())

while True:
    a = input("Enter message :")
    sock.send(str.encode(a))