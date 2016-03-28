import socket

listener = socket.socket()
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(('', 8082))
listener.listen(5)
while True:
    s, addr = listener.accept()
    request = s.recv(10000)
    print 'request text:', request
    method, rest = request.split(' ', 1)
    path, rest = rest.split(None, 1)
    print 'method:', method
    print 'path:', path
    s.send('HTTP/1.0 200 OK\n')
    s.send('Content-Type text/html')
    #s.send('Content-Type: application/octet-stream')
    #s.send('Content-Type: text/plain')
    s.send('\n\n')
    s.send('<html><body>')
    s.send('<h1>you asked to '+method+' '+path+'</h1>')
    s.send('</body></html>')
    s.close()
