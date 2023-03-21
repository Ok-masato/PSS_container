# conda install -c conda-forge opencv
import argparse
from tkinter import *
import os
import class_app
import functions

'''
mainファイル

ーー流れーーーーーーーーーー
・画像格納用フォルダの用意
・画像撮影開始
・分類
・Firebaseアップロード
ーーーーーーーーーーーーーー

# 元もOpenCVのバージョンは4.0．0.23とかやった

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


input_dir = "./imgs/img/"
diff_dir = "./imgs/Diff_img/"
out_dir = "./imgs/Diff_detect_img/"
obj_dir = "./imgs/obj_img/"
back_img_dir = "./imgs/back_img/"
obj_db = "./imgs/obj_db/"
obj_db_target = "./imgs/obj_db/target/"
trace_data = "./train_data/trace.txt"

# 認識カメラ数
NOC = functions.number_of_cameras()
ImgNumList = []  # img_numの代わり
for n in range(NOC):
    ImgNumList.append(0)
print(ImgNumList)

back_flag = False
human_flag = False
human_flag2 = False
camera_scale = 1.

# 複数カメラ用
camera_0 = 0
camera_1 = 1
flag = True
captures = []

# 画像格納用フォルダの用意
functions.folders(input_dir, diff_dir, out_dir, obj_dir, back_img_dir, obj_db, obj_db_target)

class_app.App("Sahasra Difference Detector ", input_dir, diff_dir, out_dir, obj_dir, back_img_dir, obj_db, trace_data,
    0, 0, back_flag, captures, camera_0, camera_1)