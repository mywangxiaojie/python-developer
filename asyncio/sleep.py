# Python3.7
# 新增Sleeping
# coroutine asyncio.sleep(delay,result=None,* ,loop=None)
# 阻塞delay秒，例如delay=3，则阻塞3秒。
# 如果指定了result参数的值，则在协程结束时，将该值返回给调用者。
# sleep()通常只暂停当前task，并不影响其他task的执行。
# 不建议使用loop参数，因为Python计划在3.10版本中移除它。
# 以下是一个协程的例子，功能是在5秒钟内，每秒显示一次当前的日期：
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)
    asyncio.run(display_date())

# 执行结果大致如下：
# 2018-11-20 11:27:15.961830
# 2018-11-20 11:27:16.961887
# 2018-11-20 11:27:17.961944
# 2018-11-20 11:27:18.962001
# 2018-11-20 11:27:19.962059
# 2018-11-20 11:27:20.962116并发执行Tasks