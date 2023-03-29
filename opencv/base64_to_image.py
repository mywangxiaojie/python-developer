import base64
import cv2
import numpy as np

def base64_to_image(base64_code):
 
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.fromstring(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
 
    return img

if __name__ == "__main__":
    base64 = ''
    base64_to_image(base64_code=base64)