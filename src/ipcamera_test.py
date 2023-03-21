import av
import numpy as np
import cv2

# IPカメラ1の設定
CAMERA_URL1 = "rtsp://admin:123456@114.151.100.188:554/live/jpeg/"
# cam_url_1 = "rtsp://admin:123456@192.168.11.16/live/main/"

# IPカメラ2の設定
CAMERA_URL2 = "rtsp://admin:123456@114.151.100.188:555/live/jpeg/"
# cam_url_2 = "rtsp://admin:123456@192.168.11.17/live/main/"

# カメラ1とカメラ2のキャプチャーを開始する
cap_1 = cv2.VideoCapture(cam_url_1)
cap_2 = cv2.VideoCapture(cam_url_2)
# cv2.CAP_DSHOW

# フォーマット・解像度・FPSの設定
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap_1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap_1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap_1.set(cv2.CAP_PROP_FPS, 30)

cap_2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap_2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap_2.set(cv2.CAP_PROP_FPS, 30)

# キャプチャーが正常に開始されたかどうかを確認する
if not cap_1.isOpened() or not cap_2.isOpened():
    print("Error opening video stream or file")

# カメラ1とカメラ2のウィンドウを作成する
cv2.namedWindow('Camera 1', cv2.WINDOW_NORMAL)
cv2.namedWindow('Camera 2', cv2.WINDOW_NORMAL)

# 並べて表示するためのウィンドウを作成する
cv2.namedWindow('Cameras', cv2.WINDOW_NORMAL)

# 2つのカメラから映像を取得し、1つの画面に並べて表示する
while True:
    # カメラ1から1フレーム取得する
    ret_1, frame_1 = cap_1.read()
    # カメラ2から1フレーム取得する
    ret_2, frame_2 = cap_2.read()

    # # 2つのフレームを横に並べる
    frames = cv2.hconcat([frame_1, frame_2])

    # 画面に表示する
    # cv2.imshow('Camera1', frame_1)
    # cv2.imshow('Camera2', frame_2)
    cv2.imshow('Cameras', frames)


    # キー入力を待つ
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# メモリを解放する
cap_1.release()
cap_2.release()
cv2.destroyAllWindows()