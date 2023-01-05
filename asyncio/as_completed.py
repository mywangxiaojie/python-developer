# asyncio.as_completed(aws,*,loop=None,timeout=None)
# 并发执行aws中的awaitable对象。返回一个Future对象迭代器。每次迭代时返回的Future对象代表待执行的awaitable对象集合里最早出现的结果。注意：迭代器返回的顺序与aws列表的顺序无关，只与结果出现的早晚有关。
# 如果超时之前还有Future对象未完成，则引发asyncio.TimeoutError异常。

# 用法示例：
# for f in as_completed(aws):
#     earliest_result = await f
# ...
# 以下为一个完整的例子：
import asyncio
import time


async def eternity(delay):
    await asyncio.sleep(delay)
    print(f"delay for {delay} seconds.")
    return delay

async def main():
    print(f"Start at: {time.strftime('%X')}")
    tasks = [eternity(i) for i in range(10)]
    for f in asyncio.as_completed(tasks):
        res = await f
        print(f"End at: {time.strftime('%X')}")

asyncio.run(main())
# 执行结果如下：
# Start at: 17:19:11
# delay for 0 seconds.
# delay for 1 seconds.
# delay for 2 seconds.
# delay for 3 seconds.
# delay for 4 seconds.
# delay for 5 seconds.
# delay for 6 seconds.
# delay for 7 seconds.
# delay for 8 seconds.
# delay for 9 seconds.
# End at: 17:19:20