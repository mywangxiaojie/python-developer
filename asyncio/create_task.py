# asyncio.create_task(coro)

# 将coro参数指定的协程（coroutine）封装到一个Task中，并调度执行。返回值是一个Task对象。
# 任务在由get_running_loop()返回的事件循环（loop）中执行。如果当前线程中没有正在运行的事件循环，将会引发RuntimeError异常:
import asyncio
async def coro_1():
    print("do somthing")

task = asyncio.create_task(coro_1())
# 因为当前线程中没有正运行的事件循环，所以引发异常：
# Traceback (most recent call last):
# File "C:\Program Files\Python37\lib\site-packages\IPython\core\interactiveshell.py", line 3265, in run_code
# exec(code_obj, self.user_global_ns, self.user_ns)
# File "<ipython-input-4-456c15a4ed16>", line 1, in <module>
# task = asyncio.create_task(coro_1())
# File "C:\Program Files\Python37\lib\asyncio\tasks.py", line 324, in create_task
# loop = events.get_running_loop()
# RuntimeError: no running event loop

# 对以上代码稍作修改，创建main()方法，在其中创建Task对象，然后在主程序中利用asyncio.run()创建事件循环：
import asyncio
async def coro():
    print("something is running")

async def main():
    task = asyncio.create_task(coro())
    print(asyncio.get_running_loop())

asyncio.run(main())
# 执行结果如下：
# <_WindowsSelectorEventLoop running=True closed=False debug=False>
# something is running
# 此函数已经被引入到Python3.7。在Python早期版本中，可以使用底层函数asyncio.ensure_future()代替。

async def coro():
    ...

# In Python 3.7+
task = asyncio.create_task(coro())

# This works in all Python versions but is less readable
task = asyncio.ensure_future(coro())