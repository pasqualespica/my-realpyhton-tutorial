# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)


# But a program whose threads are entirely CPU-bound, 
# e.g., a program that processes an image in parts using threads, would not 
# only become single threaded due to the lock but will also see an increase 
# in execution time, as seen in the above example, in comparison to a scenario 
# where it was written to be entirely single-threaded.

# !!! This increase is the result of acquire and release overheads added by the lock.
