import asyncio
# Tasks are used to schedule coroutines concurrently.

# When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:


async def nested():
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
    # print(task.result())

asyncio.run(main())
