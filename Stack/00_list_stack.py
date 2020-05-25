myStack = []

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)


print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())



'''

Unfortunately, list has a few shortcomings compared to other data structures you’ll look at. 

1.  The biggest issue is that it can run into speed issues as it grows. 
    The items in a list are stored with the goal of providing fast access to random elements in the list. At a high level, this means that the items are stored next to each other in memory.

2.  If your stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations. 
    This can lead to some .append() calls taking much longer than other ones.

3.  There is a less serious problem as well. 
    If you use .insert() to add an element to your stack at a position other than the end, it can take much longer. This is not normally something you would do to a stack, however.

'''
