# 基于生成器的协程（Generator-based Coroutines）
# 提示：对基于生成器的协程的支持将在Python3.10中移除，不建议使用。
# 基于生成器的协程是早期的异步实现方式，出现在async/await语法之前，使用yield from表达式等待Future或其他协程。

# 基于生成器的协程应该用@asyncio.coroutine来修饰，尽管这不是强制的。

# @asyncio.coroutine
# 基于生成器的协程的修饰器。
# 这个修饰器能使传统的基于生成器的协程与async/await语法兼容：
# @asyncio.coroutine

import asyncio

def old_style_coroutine():
    yield from asyncio.sleep(1)

async def main():
    await old_style_coroutine()

# 此修饰器将在Python3.10中被移除，所以不建议再使用。
# 此修饰器不能用于async def的协程中。asyncio.iscoroutine(obj)
# 如果obj对象是一个coroutine对象，则返回True。
# 此方法与inspect.iscoroutine()不同，因为它对基于生成器的协程也返回True。asyncio.iscoroutinefunction(func)
# 如果func是一个coroutine方法，则返回True。
# 此方法inspect.iscoroutinefunction()不同，因为它对用@coroutine修饰的基于生成器的协程也返回True。