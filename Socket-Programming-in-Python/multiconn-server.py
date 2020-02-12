#!/usr/bin/env python3

import sys
# select() allows you to check for I/O completion on more than one socket.
# So you can call select() to see which sockets have I/O ready for reading
# and/or writing. But this is Python, so there’s more.
# We’re going to use the selectors module in the standard library
# so the most efficient implementation is used, regardless of
# the operating system we happen to be running on:
# https://realpython.com/python-gil/
# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor
# https://docs.python.org/3/library/concurrent.futures.html
import socket
import selectors
import types

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    print("accept_wrapper___START")
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    print("accept_wrapper___STOP")


def service_connection(key, mask):
    print("service_connection___START")
    sock = key.fileobj  # socket object
    data = key.data  # contains the events that are ready.

    # If the socket is ready for reading, then mask & selectors.EVENT_READ 
    # is true, and sock.recv() is called. Any data that’s read is appended 
    # to data.outb so it can be sent later.
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:  # block if no data is received
            # This means that the client has closed their socket, 
            # so the server should too. 
            # But don’t forget to first call sel.unregister() 
            # so it’s no longer monitored by select().
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    # DEFAULT STATE for healthy socket !!!!!
    # When the socket is ready for writing, which should always be the case 
    # for a healthy socket
    if mask & selectors.EVENT_WRITE: 
        if data.outb:  # any received data stored in data.outb is echoed to the client using sock.send()
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
    print("service_connection___STOP")


# Main ...
if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
# The biggest difference between this server and the echo
# server is the call to lsock.setblocking(False) to configure
# the socket in non-blocking mode. Calls made to this socket will no l
# onger block. When it’s used with sel.select(), as you’ll see below,
#  we can wait for events on one or more sockets and then read and write
# data when it’s ready.
lsock.setblocking(False)

# sel.register() registers the socket to be monitored with sel.select()
# for the events you’re interested in.
# For the listening socket, we want read events: selectors.EVENT_READ.
sel.register(lsock, selectors.EVENT_READ, data=None)

print(f"start... {__name__} {sys.argv[0]}")
try:
    while True:
        print("svr.......sel.select")
        events = sel.select(timeout=None)
        # returns a list of(key, events) tuples, one for each socket. 
        # key is a SelectorKey namedtuple that contains a fileobj attribute. 
        # key.fileobj is the socket object, and mask is an event mask of 
        # the operations that are ready.
        for key, mask in events:
            if key.data is None:
                # If key.data is None, then we know it’s from the listening 
                # socket and we need to accept() the connection. 
                # We’ll call our own accept() wrapper function to get the
                # new socket object and register it with the selector.
                # We’ll look at it in a moment.
                print("svr-key.data is None.......accept_wrapper")
                accept_wrapper(key.fileobj)
            else:
                # If key.data is not None, then we know it’s a client socket 
                # that’s already been accepted, and we need to service it. 
                # service_connection() is then called and passed key and mask, 
                # which contains everything we need to operate on the socket.
                print("svr.......service_connection")
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
