

# What problem did the GIL solve for Python?
#
# Python uses reference counting for memory management. 
# It means that objects created in Python have a reference count variable that
# keeps track of the number of references that point to the object. 
# When this count reaches zero, the memory occupied by the object is released.
# Let’s take a look at a brief code example to demonstrate how reference counting works:
import sys
a = []
b = a


print(f"reference counting {sys.getrefcount(a)} a.Id {id(a)} b.Id {id(b)}")

# In the above example, the reference count for the empty list object[] was 3. 
# The list object was referenced by a, b and the argument passed to sys.getrefcount().

# This reference count variable can be kept safe by adding locks to all 
# data structures that are shared across threads so that they are not modified 
# inconsistently

# Deadlocks
# But adding a lock to each object or groups of objects means multiple locks 
# will exist which can cause another problem—Deadlocks(deadlocks can only 
# happen if there is more than one lock). Another side effect would be 
# decreased performance caused by the repeated acquisition and release of locks.
