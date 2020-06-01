import asyncio
import time

async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def main():
    t = asyncio.create_task(coro([3, 2, 1]))
    t2 = asyncio.create_task(coro([10, 5, 0]))
    print('Start:', time.strftime('%X'))
    for res in asyncio.as_completed((t, t2)):
        compl = await res
        print(f'res: {compl} completed at {time.strftime("%X")}')
    print('End:', time.strftime('%X'))
    print(f'Both tasks done: {all((t.done(), t2.done()))}')

a = asyncio.run(main())
