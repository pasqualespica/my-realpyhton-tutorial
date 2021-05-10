# Socket Programming in Python (Guide)
> by Nathan Jennings  advanced python web-dev

https://realpython.com/python-sockets/

> advanced python web-dev

The orignal examples of this tutorial use Python 3.6. You can find the source code on GitHub.
https://github.com/realpython/materials/tree/master/python-sockets-tutorial

In this repo could find few modifications as comment, print, as so on

The primary socket API functions and methods in this module are:

![alt text](img/sockets-tcp-flow.png)

![alt text](img/threewayhandshakeTCP.png)

![alt text](img/conclusione-connessioneTCP.png)

```python
socket()
bind()
listen()
accept()
connect()
connect_ex()
send()
recv()
close()
```



## Useful links 

https://en.wikipedia.org/wiki/Inter-process_communication

https://en.wikipedia.org/wiki/Berkeley_sockets

https://docs.python.org/3/library/socket.html


## Useful commnad ( on macos )

```
lsof -nP -i4TCP:$PORT | grep LISTEN
```
or
``` 
netstat -an -ptcp | grep LISTEN
```
> exmaple of `netstat` output


```bash
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  127.0.0.1.65432        127.0.0.1.55672        ESTABLISHED
tcp4       0      0  127.0.0.1.55672        127.0.0.1.65432        ESTABLISHED
tcp4       0      0  127.0.0.1.65432        *.*                    LISTEN
```

## Additional resources

https://realpython.com/python-sockets/#reference

## Notes ..

The bufsize argument of 1024 used above is the maximum amount of data to be received at once. It doesn’t mean that `recv()` will return 1024 bytes.

`send()` also behaves this way. send() returns the number of bytes sent, which may be less than the size of the data passed in. You’re responsible for checking this and calling send() as many times as needed to send all of the data:


> “Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data.” (Source)

We avoided having to do this by using `sendall()`:

> “Unlike send(), this method continues to send data from bytes until either all data has been sent or an error occurs. None is returned on success.” (Source)

We have two problems at this point:

* How do we handle multiple connections concurrently?
* We need to call send() and recv() until all data is sent or received.

***

> TODO add IMAGE

host byte order (LITTLE ENDIAN or BIG ENDIAN)
network byte order (BIG ENDIAN)

This byte order is referred to as a CPU’s endianness

```bash
python3 -c 'import sys; print(repr(sys.byteorder))'
```


http://www.serverframework.com/asynchronousevents/2011/01/time-wait-and-its-design-implications-for-protocols-and-scalable-servers.html

