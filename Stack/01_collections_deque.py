
# “deck” and stands for “double-ended queue.”


# You can use the same methods on deque as you saw above for list, .append(), and .pop():
from collections import deque
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)


print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
