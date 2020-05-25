
# How to Implement a Python Stack

https://realpython.com/how-to-implement-python-stack/


What Is a Stack?
A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO. This is in contrast to a queue, which stores items in a First-In/First-Out (FIFO) manner

You’ll look at the following Python stack implementations:

- list
- collections.deque
- queue.LifoQue



## Python Stacks and Threading
Python stacks can be useful in multi-threaded programs as well, but if you’re not interested in threading, then you can safely skip this section and jump to the summary.

The two options you’ve seen so far, list and deque, behave differently if your program has threads.

To start with the simpler one, you should never use list for any data structure that can be accessed by multiple threads. list is not thread-safe.

**Note:** If you need a refresher on thread safety and race conditions, check out An Intro to Threading in Python.

