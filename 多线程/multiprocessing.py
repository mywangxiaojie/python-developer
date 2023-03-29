import multiprocessing
import os


# 进程间通信
# 当使用多个进程时，通常使用消息传递来进行进程之间的通信，并避免必须使用任何 synchronization primitives（如锁）。对于传递消息，可以使用 Pipe（用于两个进程之间的连接）或 Queue（允许多个生产者和消费者）。

# Queue 是进程、线程安全的模型

# 设置进程启动的 3 种方式
# spawn
# 父进程会启动一个全新的 Python 解释器进程。在这种方式下，子进程只能继承那些处理 run() 方法所必需的资源。典型的，那些不必要的文件描述器和 handle 都不会被继承。使用这种方式来启动进程，其效率比使用 fork 或 forkserver 方式要低得多。
# Windows 只支持 spawn 方式来启动进程，因此在 Windows 平台上默认使用这种方式来启动进程。

# fork
# 父进程使用 os.fork() 来启动一个 Python 解释器进程。在这种方式下，子进程会继承父进程的所有资源，因此子进程基本等效于父进程。这种方式只在 UNIX 平台上有效，UNIX 平台默认使用这种方式来启动进程。

# forkserver
# 如果使用这种方式来启动进程，程序将会启动一个服务器进程。在以后的时间内，当程序再次请求启动新进程时，父进程都会连接到该服务器进程，请求由服务器进程来 fork 新进程。通过这种方式启动的进程不需要从父进程继承资源。这种方式只在 UNIX 平台上有效。

# 总结
# 从上面介绍可以看出，如果程序使用 UNIX 平台（包括 Linux 和 Mac OS X），Python 支持三种启动进程的方式；但如果使用 Windows 平台，则只能使用效率最低的 spawn 方式。

# multiprocessing 模块提供了一个set_start_method() 函数，该函数可用于设置启动进程的方式（必须将这行设置代码放在所有与多进程有关的代码之前）。


def foo(q):
    print('被启动的新进程: (%s)' % os.getpid())
    q.put('Python')

if __name__ == '__main__':
    # 设置使用fork方式启动进程
    multiprocessing.set_start_method('fork')
    q = multiprocessing.Queue()
    # 创建进程
    mp = multiprocessing.Process(target=foo, args=(q, ))
    # 启动进程
    mp.start()
    # 获取队列中的消息
    print(q.get())
    mp.join()