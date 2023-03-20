"""
PythonのOpenCVを使用して、2つのIPカメラをRTSP経由で接続し、画面に表示します
IPカメラのIPアドレス、ポート番号、ユーザー名、パスワードを適切に設定してください。
"""
import cv2

# IPカメラ1の設定
cam1_url = "rtsp://admin:123456@106.138.84.11:554/live/main"
cam1 = cv2.VideoCapture(cam1_url)

# IPカメラ2の設定
cam2_url = "rtsp://admin:123456@106.138.84.11:554/live/main"
cam2 = cv2.VideoCapture(cam2_url)

while True:
    # カメラ1の画像を取得
    ret1, frame1 = cam1.read()

    # カメラ2の画像を取得
    ret2, frame2 = cam2.read()

    # 画像が正常に取得できた場合
    if ret1 and ret2:
        # 画像を表示
        cv2.imshow('Camera 1', frame1)
        cv2.imshow('Camera 2', frame2)
    else:
        print("Failed to open camera!")
        exit()


    # キー入力を待つ
    key = cv2.waitKey(1)

    # 'q'キーが押された場合、プログラムを終了
    if key == ord('q'):
        break

# カメラを解放
cam1.release()
cam2.release()

# 画面を閉じる
cv2.destroyAllWindows()
