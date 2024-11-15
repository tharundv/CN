import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',1234))

print("*"*50)
print("Started Listening...")
while(True):
    data, addr = sock.recvfrom(1024)
    print(f"Received Message {addr}: ", data.decode())