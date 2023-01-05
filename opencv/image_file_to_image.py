import cv2
import numpy as np

def image_to_img(img_file):
    #先读取图片为字节，再转图片array
    with open(img_file, "rb") as f:
        img_data = f.read()
        img = cv2.imdecode(np.fromstring(img_data, dtype=np.uint8), 1)
        return img


def image_to_img(img_path):
    #采用numpy的fromfile
    img_path = r"test.jpg"
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    return img
   

def image_to_img(img_path):
    #采用numpy的fromfile
    # 中文路径
    img_file = "图片测试.jpg"
    new_img = cv2.imdecode(np.fromfile(img_file, dtype=np.uint8), 1)

    # 写入中文路径
    cv2.imencode('.jpg', new_img)[1].tofile(img_path)

    return new_img