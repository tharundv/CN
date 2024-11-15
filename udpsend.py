import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('127.0.0.1',1234))

while(True):
    print("Enter a Message To send : ")
    a = input("=>")
    sock.send(str.encode(a))