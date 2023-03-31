# 由网络条件不好导致“接收图片的速度”过慢导致的延迟。解决方法：

# 减少视频流大小：降低帧率、减小画幅、降低码流、主码流→辅码流、H264→H265等
# 清空摄像头缓存：刷新与摄像头的连接，重新运行 cap = cv2.VideoCapture(***)
# 问题分析：工作中的摄像头会把未被接受的视频流保存在自己的缓存里，如果缓存满了它就会报错（接收端会有xxxxxxxx sRGB xxxx 之类的报错）。只要清空摄像头缓存，就能解决这个问题，因此我们可以刷新与网络摄像头的连接 来掩盖这个问题。

# 能够应对网络延迟的视频流协议应该是：RTMP、WebRTC 之类的协议。

import cv2


def image_put(rtsp: str):
    while True:
        cap = cv2.VideoCapture(rtsp)  # 重连可以清除rtsp服务端的缓存
        if not cap.isOpened():
            print("Error: Could not open file: %s" % (rtsp))
            continue
    
        while True:
            retval, frame = cap.read()
            if not retval:
                print("Video file finished. Total Frames: %d" % (cap.get(cv2.CAP_PROP_FRAME_COUNT)))
                break
            if frame is None:
                break
            
            print("帧数据", frame)
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    image_put("rtsp://admin:admin123456@172.20.114.26/cam/realmonitor?channel=1&subtype=0")