import asyncio

# current_task()
asyncio.current_task(loop=None)
# 返回事件循环中正在运行的Task实例，如果没有Task在执行，则返回None。
# 如果loop为None，则使用get_running_loop()获取当前事件循环。
# 新增于Python3.7

# all_tasks()
asyncio.all_tasks(loop=None)
# 返回事件循环中尚未运行结束的Task对象集合。
# 如果loop为None，则使用get_running_loop()获取当前事件循环。
# 新增于Python3.7


# Task对象
# class asyncio.Task(coro,*,loop=None)
# 类似与Future对象，用于执行Python协程。非线程安全。
# Tasks用于在事件循环中执行协程。如果协程等待一个Future，那么Task会暂停协程的执行，直到Future执行完成。当Future完成时，协程的执行会恢复。
# 事件循环的 协作调度 模式：一个事件循环同一时间只执行一个Task。当这个Task等待某个Future返回时，事件循环执行其他的Task、回调或IO操作。
# 可以通过高层函数asyncio.create_task()创建Task，或者通过底层函数loop.create_task()和ensure_future()创建Task。但是不建议直接实例化Task对象。
# 如果想要取消一个Task的执行，可以使用cancel()方法。调用cancel()会引起Task对象向被封装的协程抛出CancelledError异常。当取消行为发生时，如果协程正在等待某个Future对象执行，该Future对象将被取消。
# cancelled()方法用于检查某个Task是否已被取消。如果Task封装的协程没有阻止CancelledError异常，且Task确实被取消了，则该方法返回True。
# asyncio.Task继承了Future类中除Future.set_result()和Future.set_exception()以外的所有方法。
# Task对象支持contextvars模块：当一个Task被创建的时候，它会复制当前的上下文，然后在复制的上下文副本中执行协程。
# Python3.7中的变更：添加了对contextvars模块的支持。