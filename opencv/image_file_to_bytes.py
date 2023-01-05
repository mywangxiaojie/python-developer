import cv2

def ima_path_to_bytes(img_path: str):
    img = cv2.imread(img_path)
    imgbytes = cv2.imencode(".jpg", img)[1].tobytes()