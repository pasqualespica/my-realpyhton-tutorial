import asyncio
import time

# The asyncio.create_task() function 
# 
# to run coroutines concurrently as asyncio Tasks.
# Let’s modify the above example and run two say_after coroutines concurrently:

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    start_time = time.time()
    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    duration = time.time() - start_time
    print(f"finished at {time.strftime('%X')} duration {duration} sec")

asyncio.run(main())
