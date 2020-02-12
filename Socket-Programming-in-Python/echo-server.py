#!/usr/bin/env python3

import socket

# host can be a hostname, IP address, or empty string. If an IP address is used, 
# host should be an IPv4-formatted address string. The IP address 127.0.0.1 is 
# the standard IPv4 address for the loopback interface, so only processes on the 
# host will be able to connect to the server. If you pass an empty string, 
# the server will accept connections on all available IPv4 interfaces.

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# The arguments passed to socket() specify the address family and socket type. 
# AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket 
# type for TCP, the protocol that will be used to transport our messages in 
# the network.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind() is used to associate the socket with a specific network interface and port number:
    # The values passed to bind() depend on the address family of the socket. 
    # In this example, we’re using socket.AF_INET (IPv4). So it expects a 2-tuple: (host, port).
    s.bind((HOST, PORT))
    # Continuing with the server example, listen() enables a server to accept() connections. 
    # It makes it a “listening” socket:

    # listen() has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections
    # If your server receives a lot of connection requests simultaneously, 
    # increasing the backlog value may help by setting the maximum length 
    # of the queue for pending connections. 
    # The maximum value is system dependent
    # https: // serverfault.com/questions/518862/will-increasing-net-core-somaxconn-make-a-difference/519152

    s.listen()
    # accept() blocks and waits for an incoming connection
    # When a client connects, it returns a new socket object representing the connection 
    # and a tuple holding the address of the client. 
    # The tuple will contain(host, port) for IPv4 connections
    #  or (host, port, flowinfo, scopeid) for IPv6. 
    conn, addr = s.accept()
    # Blocking Calls
    # A socket function or method that temporarily suspends your
    #  application is a blocking call.
    #  For example, accept(), connect(), send(), and recv() “block.”
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # infinite while loop is used to loop over blocking calls to conn.recv().
            # If conn.recv() returns an empty bytes object, b'', 
            # then the client closed the connection and the loop is terminated. 
            # The with statement is used with conn 
            # to automatically close the socket at the end of the block
            if not data:
                break
            # “Unlike send(), this method continues to send data from bytes until either 
            # all data has been sent or an error occurs. None is returned on success.”
            conn.sendall(data)
