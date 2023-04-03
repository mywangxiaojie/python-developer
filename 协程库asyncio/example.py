#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio

# 最简单的协程创建

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

# 使用asyncio.run()执行协程。一般用于执行最顶层的入口函数，如main()。
asyncio.run(main())


# 需要注意的是：如果像执行普通代码一样直接调用main()，只会返回一个coroutine对象，main()方法内的代码不会执行：
# <coroutine object main at 0x0000000002C97848>

import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main1():
    print(f"started at {time.strftime('%X')}")
    # await一个协程。一般用于在一个协程中调用另一协程。
    await say_after(1,"hello")
    await say_after(2,"world")
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main1())


async def main2():
    # 用asyncio.create_task()方法将Coroutine（协程）封装为Task（任务）
    task1 = asyncio.create_task(say_after(1,"hello"))
    task2 = asyncio.create_task(say_after(2,"world"))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

# 执行asyncio程序
# asyncio.run(coro, * , debug=False)
# 这个函数运行coro参数指定的 协程，负责 管理asyncio事件循环 ， 终止异步生成器。
# 在同一个线程中，当已经有asyncio事件循环在执行时，不能调用此函数。
# 如果debug=True，事件循环将运行在 调试模式。
# 此函数总是创建一个新的事件循环，并在最后关闭它。建议将它用作asyncio程序的主入口，并且只调用一次。
# Python3.7新增
# 重要：这个函数是在Python3.7被临时添加到asyncio中的。





















