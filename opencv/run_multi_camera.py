import cv2
import multiprocessing as mp
import time

# 完整版 Demo（使用多进程队列，解决延迟卡顿问题，读取多个摄像头）
# 由“处理图片的速度”慢于“摄像头拍摄产生实时图像的速度”所导致的延迟

# 关键部分解释：使用 Python3 自带的多进程模块，创建一个队列，进程 A 从通过 rtsp 协议从视频流中读取出每一帧，并放入队列中，进程 B 从队列中将图片取出，处理后进行显示。
# 进程 A 如果发现队列里有两张图片（证明进程 B 的读取速度跟不上进程 A），那么进程 A 主动将队列里面的旧图片删掉，换上新图片。
# 通过多进程的方法：进程 A 的读取速度始终不受进程 B 的影响，防止网络摄像头的缓存区爆满, 进程 A 更新了队列中的图片，使进程 B 始终读取到最新的画面，降低了延迟

def image_put(q, user, pwd, ip, channel=1):
    cap = cv2.VideoCapture("rtsp://%s:%s@%s//Streaming/Channels/%d" % (user, pwd, ip, channel))
    if cap.isOpened():
        print('HIKVISION')
    else:
        cap = cv2.VideoCapture("rtsp://%s:%s@%s/cam/realmonitor?channel=%d&subtype=0" % (user, pwd, ip, channel))
        print('DaHua')

    while True:
        q.put(cap.read()[1])
        q.get() if q.qsize() > 1 else time.sleep(0.01)

def image_get(q, window_name):
    cv2.namedWindow(window_name, flags=cv2.WINDOW_FREERATIO)
    while True:
        frame = q.get()
        cv2.imshow(window_name, frame)
        cv2.waitKey(1)

def run_single_camera():
    user_name, user_pwd, camera_ip = "admin", "admin123456", "172.20.114.26"

    # 设置用于启动子进程的方法。方法可以是’fork’，‘spawn’或’forkserver’。请注意，该法最多调用一次
    mp.set_start_method(method='spawn')  # init
    queue = mp.Queue(maxsize=2)
    processes = [mp.Process(target=image_put, args=(queue, user_name, user_pwd, camera_ip)),
                 mp.Process(target=image_get, args=(queue, camera_ip))]

    [process.start() for process in processes]
    [process.join() for process in processes]

def run_multi_camera():
    # user_name, user_pwd = "admin", "password"
    user_name, user_pwd = "admin", "admin123456"
    camera_ip_l = [
        "172.20.114.26",  # ipv4
        "[fe80::3aaf:29ff:fed3:d260]",  # ipv6
    ]

    mp.set_start_method(method='spawn')  # initv  以spawn方式启动进程 （注意还有fork/forkserver方式，不支持windows）
    queues = [mp.Queue(maxsize=4) for _ in camera_ip_l]

    processes = []
    for queue, camera_ip in zip(queues, camera_ip_l):
        processes.append(mp.Process(target=image_put, args=(queue, user_name, user_pwd, camera_ip)))
        processes.append(mp.Process(target=image_get, args=(queue, camera_ip)))

    for process in processes:
        process.daemon = True
        process.start()    # 启动进程
    for process in processes:
        process.join()



# 解决实时读取延迟卡顿的关键代码
# import multiprocessing as mp
# ...
# imgqueues = [mp.Queue(maxsize=2) for  in camera_ip_l]  # queue
# ...
# q.put(frame) if is_opened else None  # 线程A不仅将图片放入队列
# q.get() if q.qsize() > 1 else time.sleep(0.01) # 线程A还负责移除队列中的旧图
# ...

# 进程间通信
# 当使用多个进程时，通常使用消息传递来进行进程之间的通信，并避免必须使用任何 synchronization primitives（如锁）。
# 对于传递消息，可以使用 Pipe（用于两个进程之间的连接）或 Queue（允许多个生产者和消费者）。
# Queue 是进程、线程安全的模型
# 具体参考 multiprocessing


if __name__ == '__main__':
    # run_single_camera()
    run_multi_camera()
    pass