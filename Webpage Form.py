import socket
filee = open('parse.txt', 'r')

s = socket.socket()         # Create a socket object
host = socket.getfqdn()     # Get local machine name
port = 8080
s.bind((host, port))        # Bind to the port

print('Starting server on', host, port)
print('The Web server URL for this would be http://%s:%d/main.html' % (host, port))

s.listen(5)                 # Now wait for client connection.

print('Entering infinite loop; hit CTRL-C to exit')
file = open("main.html")
ok = open("OK.html")
notok = open("NOT_OK.html")
# a=''
while True:
    # Establish connection with client.
    c, (client_host, client_port) = s.accept()
    print('Got connection from', client_host, client_port)
    a = c.recv(1000) # should receive request from client. (GET ....)
    c.send('HTTP/1.0 200 OK\n'.encode())
    c.send('Content-Type: text/html\n'.encode())
    c.send('\n'.encode()) # header and body should be separated by additional newline
    for i in file:
        c.send(i.encode())
    print(a)

    try:
        if a.index(b'firstname=') > 0:
            findex = a.index(b'firstname=') + 10
            endfindex = a.index(b'&lastname=')
            firstname=  a[findex:endfindex]
            endlindex = a.index(b' HTTP')
            lastname=  a[endfindex+10:endlindex]

            found = False
            for line in filee:
                if firstname.decode() and lastname.decode() in line:
                    found = True

            if found == True:
                for k in ok:
                    c.send(k.encode())
            else:
                for j in notok:
                    c.send(j.encode())
    except:
        continue



