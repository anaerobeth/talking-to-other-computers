import socket

s = socket.socket()
s.connect(('www.google.com', 80))

s.send(b'GET /\n\n')
print(s.recv(10000))

