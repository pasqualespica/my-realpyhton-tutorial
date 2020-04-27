import asyncio
import time

# Awaiting on a coroutine. 
# 
# The following snippet of code will print “hello” 
# after waiting for 1 second, and then print “world” after waiting 
# for another 2 seconds

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    start_time = time.time()
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    duration = time.time() - start_time
    print(f"finished at {time.strftime('%X')} duration {duration} sec")

asyncio.run(main())
