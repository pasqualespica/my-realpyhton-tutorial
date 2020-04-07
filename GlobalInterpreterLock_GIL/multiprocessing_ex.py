from multiprocessing import Pool
import time

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)


# A decent performance increase compared to the multi-threaded version, right?

# The time didn’t drop to half of what we saw above because process management 
# has its own overheads. Multiple processes are heavier than multiple threads, 
# so, keep in mind that this could become a scaling bottleneck.
