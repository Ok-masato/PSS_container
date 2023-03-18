import os
import cv2

'''
input_dir:撮影画像
diff_dir：差分画像
out_dir：差分矩形を足した画像
output_txt_path:差分によって発見された矩形の位置（画像内の座標）情報
obj_dir : 画面に映っている物の画像が保存されている
back_img_dir : 差分の裏側の画像
obj_db : 物のデータベース
img_num : 画像の枚数（0が最初の背景になる）
mode : 過去のデータを読み込むかどうか
out_test : 教師データの場所
'''


# 初期フォルダ作成
def folders(*folders_path):
    for folder_path in folders_path:
        print(folder_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
            print(folder_path + " Folder created.")
    print("--- Folders for all images are set up ---")


# 接続カメラ数
def number_of_cameras():
    i = 0
    flag = True
    while flag:
        capture = cv2.VideoCapture(i)
        ret, frame = capture.read()
        flag = ret
        if flag:
            i += 1
    i -= 1
    return i

