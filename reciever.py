import socket
import threading
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('0.0.0.0',1234))
sock.listen()

def ad(session,addr):
    print(addr)
    session.send(b'Connected')
    while True:
        data = session.recv(1024)
        print(data.decode())


while True:
    s,a = sock.accept()
    t = threading.Thread(target=ad,args=(s,a))
    t.start()