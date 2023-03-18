import cv2

# IPカメラのURLを設定
url = "rtsp://admin:123456@106.138.84.11:554/live/main"

# OpenCVでカメラを開く
cap = cv2.VideoCapture(url)

# カメラが開かれているか確認
if not cap.isOpened():
    print("Failed to open camera!")
    exit()

# 画像の表示
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # 'q'を押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラを解放し、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()