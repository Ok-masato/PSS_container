# conda install -c conda-forge opencv
import cv2
import argparse
from libs import DiffCreate, RefleshFolder
from tkinter import *
from PIL import Image, ImageTk
import human_detector
import numpy as np
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "--mode", type=str, default="first",
    help="mode: first or load"
)

args = parser.parse_args()


class App:
    def __init__(self, window_title, input_dir, diff_dir, out_dir, obj_dir,
                 back_img_dir, obj_db, trace_data, img_num_0, img_num_1, back_flag, captures, camera_0, camera_1):

        """
        # self.vcap_0 = cv2.VideoCapture(0)
        # self.vcap_1 = cv2.VideoCapture(1)
        """
        # IPカメラ用
        self.vcap_0 = cv2.VideoCapture("rtsp://admin:123456@114.151.100.188:554/live/jpeg/")
        self.vcap_1 = cv2.VideoCapture("rtsp://admin:123456@114.151.100.188:555/live/jpeg/")


        # カメラの焦点操作。実験環境にあわせて調整してください。
        self.vcap_0.set(cv2.CAP_PROP_FOCUS, 10)
        self.vcap_1.set(cv2.CAP_PROP_FOCUS, 10)

        WIDTH = 1280
        HEIGHT = 720
        self.vcap_0.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.vcap_0.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap_0.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        self.vcap_1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.vcap_1.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap_1.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

        self.yolo = human_detector.YOLO()
        self.human_exist = [False, False, False, False]

        self.img_num_0 = img_num_0
        self.img_num_1 = img_num_1
        self.camera_0 = camera_0
        self.camera_1 = camera_1
        self.input_dir = input_dir
        self.back_flag = back_flag
        self.trace_data = trace_data

        self.dc_0 = DiffCreate.DiffCreate(input_dir, diff_dir, out_dir,
                                        obj_dir, back_img_dir, obj_db, trace_data, img_num_0, camera_0)
        self.dc_1 = DiffCreate.DiffCreate(input_dir, diff_dir, out_dir, obj_dir, back_img_dir, obj_db, trace_data,
                                         img_num_1, camera_1)


        self.capture()

        while True:
            # update()関数を15ミリ秒ごとに呼び出し、
            # キャンバスの映像を更新する
            self.delay = 15
            self.update()

        # self.window.mainloop()

    def check_capture(self):
        if (self.human_exist[0] == True) and (self.human_exist[1] == False) and (self.human_exist[2] == False) \
                and (self.human_exist[3] == False):
            return True
        else:
            return False

    # キャンバスに表示されているカメラモジュールの映像を
    # 15ミリ秒ごとに更新する
    def update(self):
        ret_0, image_0 = self.vcap_0.read()
        ret_1, image_1 = self.vcap_1.read()
        # 保存用のイメージ
        tmp_image_0 = image_0
        tmp_image_1 = image_1
        rh = 720
        rw = 1280

        image_0 = cv2.resize(image_0, (rw, rh))
        image_0 = image_0[:, :, (2, 1, 0)]
        image_0 = Image.fromarray(image_0)
        # ここでエラーが発生する際、どちらかのウェブカメラの映像が来ていない
        # 接続するUSBポートの変更で解決した
        image_1 = cv2.resize(image_1, (rw, rh))
        image_1 = image_1[:, :, (2, 1, 0)]
        image_1 = Image.fromarray(image_1)

        r_image_0, human_flag_0 = self.yolo.detect_image(image_0)
        r_image_1, human_flag_1 = self.yolo.detect_image(image_1)

        del self.human_exist[0]
        self.human_exist.append(human_flag_0)
        print(self.human_exist)

        if self.back_flag and self.check_capture():
            path_0 = self.input_dir + str(self.img_num_0) + "-" + str(self.camera_0) + ".jpg"
            path_1 = self.input_dir + str(self.img_num_1) + "-" + str(self.camera_1) + ".jpg"

            cv2.imwrite(path_0, tmp_image_0)  # 画像ファイル(input_dir)に保存
            cv2.imwrite(path_1, tmp_image_1)

            done_0 = self.dc_0.detect_contour()
            done_1 = self.dc_1.detect_contour()
            if done_0:
                self.img_num_0 = self.img_num_0 + 1
                self.dc_0.plus_num()

            if done_1:
                self.img_num_1 = self.img_num_1 + 1
                self.dc_1.plus_num()

            print("Success this capture num ({}).".format(self.img_num_0))


    # Closeボタンの処理
    def destructor(self):
        print("Quit.")
        self.window.destroy()
        self.vcap_0.release()
        self.yolo.close_session()

    # 撮影ボタンの処理
    def capture(self):
        path_0 = self.input_dir + str(self.img_num_0) + "-" + str(self.camera_0) + ".jpg"
        path_1 = self.input_dir + str(self.img_num_1) + "-" + str(self.camera_1) + ".jpg"

        _, frame_0 = self.vcap_0.read()
        _, frame_1 = self.vcap_1.read()

        if args.mode == "first":
            if not self.back_flag:
                self.back_flag = True
                cv2.imwrite(path_0, frame_0)  # 画像ファイル(input_dir)に保存
                cv2.imwrite(path_1, frame_1)
                self.img_num_0 = self.img_num_0 + 1
                self.img_num_1 = self.img_num_1 + 1
                self.dc_0.plus_num()
                self.dc_1.plus_num()
                # self.ref_btn['state'] = DISABLED
                print("Success capture(back).")

            # add
            else:
                cv2.imwrite(path_0, frame_0)  # 画像ファイル(input_dir)に保存
                cv2.imwrite(path_1, frame_1)
                done_0 = self.dc_0.detect_contour()
                done_1 = self.dc_1.detect_contour()
                if done_0:
                    self.img_num_0 = self.img_num_0 + 1
                    self.dc_0.plus_num()

                if done_1:
                    self.img_num_1 = self.img_num_1 + 1
                    self.dc_1.plus_num()
                print("Success this capture num ({}).".format(self.img_num_0))

        elif args.mode == "load":
            pass