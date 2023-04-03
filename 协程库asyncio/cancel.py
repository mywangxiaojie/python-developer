# 申请取消任务。
# 将在下一个事件循环周期中将CancelledError异常抛给封装在Task中的协程。
# 收到CancelledError异常后，协程有机会处理异常，甚至以try ...except CancelledError ...finally来拒绝请求。

# 因此，与Future.cancel()不同，Task.cancel()不能保证Task一定被取消掉。当然，拒绝取消请求这种操作并不常见，而且很不提倡。

# 以下例子可以说明协程如何拦截取消请求：
import asyncio

async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
# cancel_me(): before sleep
# cancel_me(): cancel sleep
# cancel_me(): after sleep
# main(): cancel_me is cancelled now


# cancelled()
# 如果Task已经被取消，则返回True。
# 当取消请求通过cancel()被提交，且Task封装的协程传播了抛给它的CancelledError异常，则此Task被取消。