import asyncio

import aioredis


async def main():
    redis = aioredis.Redis.from_url("redis://localhost")
    await redis.delete("foo", "bar")
    async with redis.pipeline(transaction=True) as pipe:
        res = await (pipe.incr("foo").incr("bar").execute())
    print(res)

    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
