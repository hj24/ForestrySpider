import asyncio

from utils.decorators import counter

@counter.counter
async def test():
    await asyncio.sleep(3)
    return 1


loop = asyncio.get_event_loop()

res = loop.run_until_complete(test())

print(res)

loop.close()