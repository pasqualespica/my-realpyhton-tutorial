import asyncio


async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def main():
    # This is a bit redundant in the case of one task
    # We could use `await coro([3, 2, 1])` on its own
    t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
    await t
    print(f't: type {type(t)}')
    print(f't done: {t.done()}')

t = asyncio.run(main())
