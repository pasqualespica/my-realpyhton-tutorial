import asyncio


# The asyncio.run() function 
#
# to run the top-level entry point “main()” function

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())


