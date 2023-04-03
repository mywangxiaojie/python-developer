# print_stack(* ,limit=None,file=None)
# 打印Task的栈帧或异常回溯。
# 此方法用于输出由get_stack()取回的帧列表，输出形式类似于回溯(traceback)模块
# limit参数会直接传递给get_stack()。
# file参数指定输出的I/O流，默认为sys.stderr。classmethod all_tasks(loop=None)
# 返回一个事件循环上所有任务的集合。


# 默认情况下，当前事件循环上所有的任务都会被返回。如果loop参数为’None’，则通过get_event_loop()方法获取当前事件循环。
# 此方法将在Python3.9中被移除，所以不建议使用。可以使用asyncio.all_tasks()代替。calssmethod current_task(loop=None)
# 返回当前正在运行的Task或None。

# 如果loop参数为’None’，则通过get_event_loop()方法获取当前事件循环。
# 此方法将在Python3.9中被移除，所以不建议使用。可以使用asyncio.current_task()代替。