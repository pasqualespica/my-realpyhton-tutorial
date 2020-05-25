'''
The answer is in the queue module, queue.LifoQueue. Remember how you learned that stacks operate on the Last-In/First-Out principle? Well, that’s what the “Lifo” portion of LifoQueue stands for.

While the interface for list and deque were similar, LifoQueue uses .put() and .get() to add and remove data from the stack:

'''

from queue import LifoQueue
myStack = LifoQueue()

myStack.put('a')
myStack.put('b')
myStack.put('c')

print(myStack)
print(myStack.get())
print(myStack.get())
print(myStack.get())
# myStack.get() <--- waits forever
print(myStack.get_nowait())
