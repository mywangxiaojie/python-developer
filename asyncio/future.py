# Future 是一种特殊的底层可等待对象，代表一个异步操作的最终结果。
# 当一个Future对象被await的时候，表示当前的协程会持续等待，直到Future对象所指向的异步操作执行完毕。
# 在asyncio中，Future对象能使基于回调的代码被用于asyn/await表达式中。

# 一般情况下，在应用层编程中，没有必要创建Future对象。
# 有时候，有些Future对象会被一些库和asyncio API暴露出来，我们可以await它们：

import asyncio

async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )