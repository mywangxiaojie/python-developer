# awaitable asyncio.gather(* aws, loop=None, return_exceptions=False)
# 并发执行aws参数指定的 可等待（awaitable）对象序列。
# 如果 aws 序列中的某个 awaitable 对象 是一个协程,则自动将这个协程封装为Task对象进行处理。例如：
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
        print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
)

asyncio.run(main())

# Expected output:
#
# Task A: Compute factorial(2)...
# Task B: Compute factorial(2)...
# Task C: Compute factorial(2)...
# Task A: factorial(2) = 2
# Task B: Compute factorial(3)...
# Task C: Compute factorial(3)...
# Task B: factorial(3) = 6
# Task C: Compute factorial(4)...
# Task C: factorial(4) = 24
# 如果所有的awaitable对象都执行完毕，则返回awaitable对象执行结果的聚合列表。返回值的顺序于aws参数的顺序一致。   
# 简单修改以上代码：
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        #print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i

    #print(f"Task {name}: factorial({number}) = {f}")
    return number

async def main():
    # Schedule three calls *concurrently*:
    print(await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
)

asyncio.run(main())

# Expected output:
#
#[2, 3, 4]#await asyncio.gather()的返回值是一个列表，
#分别对应factorial("A", 2),factorial("B", 3),factorial("C", 4)的执行结果。

# 如果return_execptions参数为False（默认值即为False），引发的第一个异常会立即传播给等待gather()的任务，即调用await asyncio.gather()对象。
# 序列中其他awaitable对象的执行不会受影响。例如：
import asyncio

async def division(divisor, dividend):
    if divisor == 0:
        raise ZeroDivisionError
    else:
        print(f"{dividend}/{divisor}={dividend/divisor}")
    return dividend/divisor

async def main():
    # Schedule three calls *concurrently*:
    print(await asyncio.gather(
        division(0, 2),
        division(1, 2),
        division(2, 2),
    ))

asyncio.run(main())
# 执行结果：
# 2/1=2.0
# 2/2=1.0
# Traceback (most recent call last):
# File "test.py", line 19, in <module>
# asyncio.run(main())
# File "c:\Program Files\Python37\lib\asyncio\runners.py", line 43, in run
# return loop.run_until_complete(main)
# File "c:\Program Files\Python37\lib\asyncio\base_events.py", line 573, in run_until_complete
# return future.result()
# File "test.py", line 16, in main
# division(2, 2),
# File "test.py", line 6, in division
# raise ZeroDivisionError
# ZeroDivisionError
# 如果return_exceptions参数为True，异常会和正常结果一样，被聚合到结果列表中返回。
# 对以上代码稍作修改，将return_exceptions设为True：
import asyncio

async def division(divisor, dividend):
    if divisor == 0:
        raise ZeroDivisionError
    else:
        print(f"{dividend}/{divisor}={dividend/divisor}")
    return dividend/divisor

async def main():
    # Schedule three calls *concurrently*:
    print(await asyncio.gather(
        division(0, 2),
        division(1, 2),
        division(2, 2),
        return_exceptions=True
    ))

asyncio.run(main())
# 执行结果如下：
# 2/1=2.0
# 2/2=1.0
# [ZeroDivisionError(), 2.0, 1.0]#错误不会向上传播，而是作为结果返回

# 如果gather()被取消，则提交的所有awaitable对象（尚未执行完成的）都会被取消。例如：
import asyncio

async def division(divisor, dividend):
    if divisor == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(divisor)
        print(f"{dividend}/{divisor}={dividend/divisor}")
    return dividend/divisor

async def main():
    # Schedule three calls *concurrently*:
    t = asyncio.gather(
        division(0, 2),
        division(1, 5),
        division(3, 6),
        return_exceptions=True
    )
    await asyncio.sleep(2)
    t.cancel()
    await t

asyncio.run(main())
# 执行结果：
# 5/1=5.0 #除已执行的之外，其他的任务全部被取消
# Traceback (most recent call last):
# File "test.py", line 23, in <module>
# asyncio.run(main())
# File "c:\Program Files\Python37\lib\asyncio\runners.py", line 43, in run
# return loop.run_until_complete(main)
# File "c:\Program Files\Python37\lib\asyncio\base_events.py", line 573, in run_until_complete
# return future.result()
# concurrent.futures._base.CancelledError
#在return_exceptions=True的情况下，异常依然向上传播。
# 如果aws中某些Task或Future被取消，gather()调用不会被取消，被取消的Task或Future会以引发CancelledError的方式被处理。这样可以避免个别awaitable对象的取消操作影响其他awaitable对象的执行。
# 例如：
import asyncio

async def division(divisor, dividend):
    if divisor == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(divisor)
        print(f"{dividend}/{divisor}={dividend/divisor}")
    return dividend/divisor

async def main():
    # Schedule three calls *concurrently*:
    task1 = asyncio.create_task(division(0, 2))
    task2 = asyncio.create_task(division(1, 5))
    task3 = asyncio.create_task(division(3, 6))
    t = asyncio.gather(
        task1,
        task2,
        task3,
        return_exceptions=True
    )
    task1.cancel()

    print(await t)

asyncio.run(main())
# 预期执行结果如下：
# 5/1=5.0
# 6/3=2.0
# [CancelledError(), 5.0, 2.0] # 仅task1被取消，其他任务不受影响。避免取消
# awaitable asyncio.shield(aw, * , loop=None)
# 防止awaitable对象被取消(cancelled)执行。
# 如果aw参数是一个协程(coroutines),该对象会被自动封装为Task对象进行处理。
# 通常，代码：
# #code 1
# res = await shield(something())
# 同代码：
# #code 2
# res = await something()
# 是等价的。
# 特殊情况是，如果包含以上代码的协程被取消，code1与code2的执行效果就完全不同了：
# 	* 
# code 1中，运行于something()中的任务 不会被取消。
# 	* 
# code 2中，运行于something()中的任务 会被取消。


# 在code1中，从something()的视角看，取消操作并没有发生。然而，事实上它的调用者确实被取消了，
# 所以await shield(something())仍然会引发一个CancelledError异常。
import asyncio
import time

async def division(divisor, dividend):
    if divisor == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(divisor)
        print(f"{time.strftime('%X')}:{dividend}/{divisor}={dividend/divisor}")
    return dividend/divisor

async def main():
    # Schedule three calls *concurrently*:
    print(f"Start time:{time.strftime('%X')}")
    task1 = asyncio.shield(division(1, 2))
    task2 = asyncio.create_task(division(1, 5))
    task3 = asyncio.create_task(division(3, 6))

    res = asyncio.gather(task1, task2, task3, return_exceptions=True)

    task1.cancel()
    task2.cancel()
    print(await res)

asyncio.run(main())
# 执行结果：
# Start time:10:38:48
# 10:38:49:2/1=2.0
# 10:38:51:6/3=2.0
# [CancelledError(), CancelledError(), 2.0]
# #task1虽然被取消，但是division(1,2)依然正常执行了。
# #task2被取消后，division(1,5)没有执行
# #虽然task1内的协程被执行，但返回值依然为CancelledError
# 如果something()以其他的方式被取消，比如从自身内部取消，那么shield()也会被取消。
# 如果希望完全忽略取消操作（不推荐这么做），则可以将shield()与try/except结合起来使用：
# try:
# res = await shield(something())
# except CancelledError:
# res = None超时（Timeouts）