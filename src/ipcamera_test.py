import cv2
import time

# カメラの設定
camera1_url = "rtsp://admin:123456@114.151.100.188:554/live/main/"
camera2_url = "rtsp://admin:123456@114.151.100.188:555/live/main/"

# カメラに接続
cap1 = cv2.VideoCapture(camera1_url)
cap2 = cv2.VideoCapture(camera2_url)

# 画像を保存するフォルダ
output_folder = "src/imgs/img/"

# 画像の取得間隔（秒）
interval = 10

# 画像を保存する関数
def save_image(frame, camera_id, timestamp):
    filename = output_folder + f"camera{camera_id}_{timestamp}.jpg"
    print(filename)
    cv2.imwrite(filename, frame)

# メインループ
while True:
    # カメラからフレームを取得
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # 両方のカメラが正常に接続されている場合
    if ret1 and ret2:
        print("true")
        # 現在時刻を取得
        timestamp = int(time.time())

        # 画像を保存
        save_image(frame1, 1, timestamp)
        save_image(frame2, 2, timestamp)

        # 一定時間待機
        time.sleep(interval)

    # カメラに接続できなかった場合
    else:
        print("Failed to connect to one or more cameras.")
        break

# カメラとの接続を解除
cap1.release()
cap2.release()
"""
import numpy as np
import cv2

# IPカメラ1の設定
CAMERA_URL1 = "rtsp://admin:123456@114.151.100.188:554/live/jpeg/"
# cam_url_1 = "rtsp://admin:123456@192.168.11.16/live/main/"

# IPカメラ2の設定
CAMERA_URL2 = "rtsp://admin:123456@114.151.100.188:555/live/jpeg/"
# cam_url_2 = "rtsp://admin:123456@192.168.11.17/live/main/"

# カメラ1とカメラ2のキャプチャーを開始する
cap_1 = cv2.VideoCapture(CAMERA_URL1)
cap_2 = cv2.VideoCapture(CAMERA_URL2)
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
"""