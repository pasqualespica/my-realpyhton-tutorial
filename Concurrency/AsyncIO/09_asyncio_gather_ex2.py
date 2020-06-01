import time
import asyncio


async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))
    
async def main():
    t = asyncio.create_task(coro([3, 2, 1]))
    t2 = asyncio.create_task(coro([10, 5, 0]))  # Python 3.7+
    print('Start:', time.strftime('%X'))
    a = await asyncio.gather(t, t2)
    print('End:', time.strftime('%X'))  # Should be 10 seconds
    print(f'Both tasks done: {all((t.done(), t2.done()))}')
    return a

a = asyncio.run(main())

# a
