# coroutine asyncio.wait_for(aw,timeout,*,loop=None)
# 在timeout时间之内，等待aw参数指定的awaitable对象执行完毕。
# 如果aw是一个协程，则会被自动作为Task处理。
# timeout可以是None也可以是一个float或int类型的数字，表示需要等待的秒数。如果timeout是None，则永不超时，一直阻塞到aw执行完毕。
# 如果达到timeout时间，将会取消待执行的任务，引发asyncio.TimeoutError.
# 如果想避免任务被取消，可以将其封装在shield()中。
# 程序会等待到任务确实被取消掉，所以等待的总时间会比timeout略大。
# 如果await_for()被取消，aw也会被取消。
# loop参数将在Python3.10中删除，所以不推荐使用。
# 示例：

import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
# timeout!
# Python3.7新特性：当aw因为超时被取消，wait_for()等到aw确实被取消之后返回异常。在以前的版本中，wait_for会立即返回异常。

# 等待原语（Waiting Primitives）wait()
# coroutine asyncio.wait(aws,*,loop=None,timeout=None,return_when=ALL_COMPLETED)
# 并发执行aws中的awaitable对象，一直阻塞到return_when指定的情况出现。
# 如果aws中的某些对象是协程（coroutine），则自动转换为Task对象进行处理。直接将coroutine对象传递给wait()会导致令人迷惑的执行结果，所以不建议这么做。
# 返回值是两个Task/Future集合:(done,pending)。
# 用法示例：
# done,pending = await asyncio.wait(aws)
# loop参数将在Python3.10中删除，所以不建议使用。
# timeout参数可以是一个int或float类型的值，可以控制最大等待时间。
# 需要注意的是，wait()不会引发asyncio.TimeoutError错误。返回前没有被执行的Future和Task会被简单的放入pending集合。
# return_when决定函数返回的时机。它只能被设置为以下常量：
# Constant
# Description
# FIRST_COMPLETED
# The function will return when any future finishes or is cancelled.
# FIRST_EXCEPTION
# The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED.
# ALL_COMPLETED
# The function will return when all futures finish or are cancelled.

# 与wait_for()不同，wait()不会再超时的时候取消任务。
# 注意：
# 因为wait()会自动将协程转换为Task对象进行处理，然后返回这些隐式创建的Task到（done,pending）集合，所以以下代码不会如预期的那样执行。
async def foo():
    return 42

coro = foo()
# done, pending = await asyncio.wait({coro})
# if coro in done:
# 因为wait()会自动将协程转换为Task对象进行处理，然后返回这些隐式创建的Task到（done,pending）集合，所以这个条件分支永远不会被执行。
# 上面的代码可以做如下修正：
async def foo():
    return 42

task = asyncio.create_task(foo())
# done, pending = await asyncio.wait({task})
# if task in done:
# 这回可以正常执行了.
# 所以，正如上文所讲，不建议将coroutine对象直接传递给wait()。