import socket

s = socket.socket()
s.connect(('18.189.123.94', 1234))
print 'Start Talking!'

while True:
    msg = raw_input('Me: ')
    s.send(msg)
    stream = s.recv(100)
    print("Response: ")
    print(stream)

