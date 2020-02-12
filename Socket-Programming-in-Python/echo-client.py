#!/usr/bin/env python3

import socket

# if you user '' and not localhost server will open on all eth
# following " netstat -an -ptcp | grep 65432 " on MacOs
# tcp4       0      0 * .65432 * .* LISTEN
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# socket.socket() creates a socket object that supports the context manager type, 
# so you can use it in a with statement. There’s no need to call s.close():
# https://docs.python.org/3/reference/datamodel.html#context-managers

# The arguments passed to socket() specify the address family and 
# socket type. AF_INET is the Internet address family for 
# IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used 
# to transport our messages in the network.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
