# 从其他线程调度执行（Scheduling From Other Threads）
# asyncio.run_coroutine_threadsafe(coro,loop)
# 向loop指定的事件循环提交一个由coro指定协程。线程安全。
# 返回一个concurrent.futures.Future对象，等待另一个线程返回结果。
# 这个函数用于从当前线程向运行事件循环的线程提交协程(coroutine)。
# 例如：

import asyncio
# Create a coroutine
coro = asyncio.sleep(1, result=3)

loop = asyncio.get_event_loop()
timeout = 3

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
# 如果协程出现异常，返回的Future会收到通知。返回的Future也可以被用作取消事件循环中的任务：
try:
    result = future.result(timeout)
except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')

# 与其他asyncio函数不同，该函数需要显式传递loop参数。
# 新增于Python 3.5.1