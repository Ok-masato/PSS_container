from webbrowser import get
import firebase_admin
from firebase_admin import credentials, db, firestore
import datetime
from google.cloud import storage
import os
import re
import glob

'''テスト用'''
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "sahasra-image",
    "private_key_id": "9da850efb3ace911598bee7ddb99383c84a14955",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDh4vjVVgrzUNT2\nVa6q7gSIWNywCFBoTvIQYU8xtRJT0ucnBqbXd93CEU+NI3ks9EAno7UgmYM/6c0H\nOEL0y8Q8gRi8PAmd4Ng1EVtZVdh+DzxzDv5+mt87dy+eaSZ4dJi1r/q5Hw9eJA7H\nruqjl61LEaXwdcdMuALnHASHtOSKc0oX9OmvIZg9ZmcPBjb5wzKcR+P6Q9SLe5UK\nRm5aTny0i9u59rjgVqQIKMnaUpG1VHP1sbmQe8YRJBw3dTtzDVXwlHF/7sgk/0jN\n7VknMZZw2Mu5AtC/B/QzTI8w6o+m8CYWxxVNuTkTkSGT2pmRb3CvMKFbYciJLVzY\npgf6A54rAgMBAAECggEAaPwgMasNaNvjNuBIz5nTUnmWjFw43tn+SF2pvI0PSRVH\nKMy/I3rK/wUjp5HaommdHa9JIi8nIL/t8lKUUAkamhJYKDhxMccMRdHc1o7/EUvM\niR9pafdaFF3HLIVrg2WRijQRwBNvBY6VrfoehM0cljzMFo/vArmtY7OSaW5KIAwo\n1KkaxmufEixHFTsGXg8WliCJGT3sSgt/Sh10o+sEaRUk7Ksch7h9m4qmndErauLe\ny69eG8reCFxVtK0xb7YB653uHEkqnRAAMKk6NpeKrDG3lSwQa5XgSm5QZQyEhiK/\nIdU+b2s8k+Yv87ukcOSXJMadGWcGNQoak2LnRM3u4QKBgQDyPfN5PHXLSLEUvkla\nSieCl+XY3mf75up5XvoRydL9DDpgdlBRSXuJ8Tc3orvk/WkPM8x/jwsC3a+elVZW\n5y0EN+5XkV0HGCnDMXbhHaV5QrxIzhqEwY65SzHmgTmroYRt8wiMFvI1odr/zCfI\n5W5WUkpjo58YIwYzlXMlauD4SwKBgQDutzlFhW5YojsiHn5+sC0DuJBkk+OQzPG/\n8uHnDE9wYIi7uZVGPtSAZPYd4YKrdRALZjIUe1/pqammOSTSPfHuEjFWpAfixqAR\nB5JcUgfaTGtXDPuOIhK3S+DlQ3yVhEX8DWbU6sTYWCAoQrykkYVpgYZECbZ2sUdz\nYOnVyEoFoQKBgQCv2nldkZ6RrHug62KkwSBdlZeuEAa8v62H3oL7VuBsAux+CmXU\nHNwqD4peQSzV14DlIF1cXKNJuVU8cnzzKW9smI3V1BkMhWYL5WS/l54AoYm98KEf\nrsPFj+jxxO3wwpg4mS2jRSUf+hfZioN3O9cVozeNjcJ46zQdTmkAyM34cQKBgQDc\nd43GXmA2LcatUTqEaNN6H0gEC+3dOtp+66OlTuJDKHS/47swwDBkUFpZ6H9VOO1T\nidPwxK0lUZOkOByAq8M3m8fDfATodYc5kyOibgRgobl1EUF22JMuhD61nul98Ubt\nbbcuJ5EbOfChHlm5J8juUzict9ezsTELJ1NvJObwYQKBgQC/HOAhYIh+kPEWs3gY\ngKpntISBNSovuPvYLspGYJGfGp5NF/274DkRHns8SucscUmMkFyGq3BxagcYXuMk\nfMqhnH/iKrUiPUO4+RE3aUx1e3whGA+KPkINHfwHqbzD5OxY/Z22FfjmPgtE5AYo\ntf16ufsZkVZZ2bPvaU1fCRwRCw==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-clww9@sahasra-image.iam.gserviceaccount.com",
    "client_id": "109461025962649718242",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-clww9%40sahasra-image.iam.gserviceaccount.com"
})

# 秘密鍵
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './sahasra-image-firebase-adminsdk-clww9-9da850efb3.json'
GOOGLE_APPLICATION_CREDENTIALS = './sahasra-image-firebase-adminsdk-clww9-9da850efb3.json'
# バケット
os.environ['FIREBASE_STORAGE_BUCKET'] = 'sahasra-image.appspot.com'
FIREBASE_STORAGE_BUCKET = "sahasra-image.appspot.com"
BACKET_NAME = "sahasra-image"

storage_client = storage.Client()
bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
''''''

'''本番用'''
# cred = credentials.Certificate({
#     "type": "service_account",
#     "project_id": "sahasura-5f7bd",
#     "private_key_id": "b0597cde9457d9614ba063e8aa9678aa62a0ec33",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuZypa3ns9xfg3\nsDwhWnfTn21drPQKYp3fGgQ0zGNXQVeYQ/j2E1oNmv7NG63PNIVSHb998mE8sRkd\neXulM37GWaFs74kgEdd5Rfej/LwVdhvPQMhLXX0UbSy/JgjzAg24Po1WtwVPVmeO\nQO5Juj80Xlo8eXnI/f1s3kJABXqoIdv1DKJKJiPA6o4jLxJNBQAg9q0YFKbfnM/X\nvdmAYGwVna5QV149vZpbXw07p1842ANcHuw+feaRT7BlVtvx9ZH7knOK5h+f1OVA\ncTlmu2uXq9kcDHF8ZWOl5NEHXvSbEnluyeW/QHN3vKynS2LdZYiGV7NYYxFXTgH/\npVE1gO2nAgMBAAECggEAMh+1ZRtnOThSIBM3HPDm2nwKDy+7jdaNAAd2qQQLExNV\nDQ6QGY0zRxDCZYmseQ5juNeS5yxHtQ1DJhz5o9+6cmBlTC1F8GEgWBr7Uva6ycJB\nuN2qEzsBzWKZRzCzxr/S2J6luYPtc0FmjtRrh+YO70qkzZeuIE2bTfRM/yB0AakL\n+FJNqSWpNE5rB/fSmCZb1Obv6ymZYColDZVOse97EP7pgwU9v0/cujaFesPBwwSC\nexAI+fZBMIYi9SBdWfiUlxih1+aPmW9jd8vEySLFwc8YtdMhTBjgTGqVGYGZZOdd\naUCBqS/0yhVSqdOBxXY8nooZtXL5BQXyZHarglFc7QKBgQDdztDA55nCdbF6LVMa\n06gQHD7kapKsKaOx8Tq1ZIjwMA5VIvC5G6jX8X3L7PnwFYuh55QcMjJDwQsrxrjM\npQCxWfZ9EyDr+Nr/5R+EJprQyRXm5SmveD0BIDxKmswVpTpxlwahkW+X32VcsA1j\ngkWgN4WF76CjKVgmHrQ80O0o+wKBgQDJSZ2DoCrNjKgpjwB45C9YemGk8doETz4Y\nxf1z4wATFJtSfcbchiOgufTwh67m0dP9DFETeYvjFw+DEsq93QoZe0WTsTVs9BY9\n9M2bD64gTNg5YTtYPQkEdYpi07/ysedpaeC01ch1aitxYoltncNQswis44AlUPqd\n9Sow360GRQKBgCzSDNbeNfDYjXttyzxBhtVyj7biXi8R3vUnFMDwxscaPtsvS0ts\nbmrsbooVoc/E2sllnUUxU3zjdllrN46KzSAJWMifY+irCb3p07uFfYUxDQ7yQcEm\nX9VpaSV+MD0zfSLU7M8bL1yWFMps/NedzGn6ri2JZYFy6lARpkQfx7yfAoGASQ1f\njkrN3gXDbjnJGRbvm/Pmhj+EOXYs+j65CpsDBum+qUSerKA+Q/HZVIZZ0smqXzde\nIWxGead/6LkkPZ4AMVlM2hpBYoZ/oAK9sB4TuwNIoiKIsDCOmkCydcWV71Xjv50+\ngULpWruqgp8Zc2ADZ8FiT6TNeD2Yh0VYB57WI+UCgYEAhR1AoqUx3iHYNX/+6XSK\nVf/CKF7yVaTCR3y+d6kW4h7QCiIi5ioczBt8u7R/ib+S0gHuh9F2Cz33HyVlCR5a\n8MJliZQi4mSMmNxaMKe6lmNinpRtE5MAEStPTzsFBu5SjaQFQHlqEzzOcPfxrHUe\nOT6KffU5OUMzRmDd+O0jsrA=\n-----END PRIVATE KEY-----\n",
#     "client_email": "firebase-adminsdk-k0iu3@sahasura-5f7bd.iam.gserviceaccount.com",
#     "client_id": "107511115899299830498",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-k0iu3%40sahasura-5f7bd.iam.gserviceaccount.com"
# })
# BUCKET_NAME = "sahasura-5f7bd.appspot.com"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "cred.json"
# storage_client = storage.Client()
# bucket = storage_client.bucket(BUCKET_NAME)
''''''



"""----------------------------------------------------------------
Firebase 処理
----------------------------------------------------------------"""
# Firebaseのイニシャライズ
def FirebaseInitialize():
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
        bucket = storage.bucket
    # print("[Success] FirebaseInitialize")



'''----------------------------------------------------------------
Firestore Databaseの処理
----------------------------------------------------------------'''
# FirestoreDatebaseのセット
def SetDB(collection, users, cameraID, classes, colors, images, objectImages, projectID, sDatetime, sTimestamp, state, timestamp, x, x0, x1, y, y0, y1, z):
    db = firestore.client()
    # print(collection, users, cameraID, classes, colors, images, objectImages, projectID, sDatetime, sTimestamp, state, timestamp, x, x0, x1, y, y0, y1, z)
    data = {
        u'cameraID': cameraID,
        u'classes': classes,
        u'colors': colors,
        u'images': images,
        u'markerID': "markerTestID",
        u'objectImages':objectImages,
        u'projectID': projectID,
        u'sDatetime': sDatetime,
        u'sTimestamp': sTimestamp,
        u'state': state,
        u'timestamp': timestamp,
        u'x': x,
        u'x0': x0,
        u'x1': x1,
        u'y': y,
        u'y0': y0,
        u'y1': y1,
        u'z': z
    }
    db.collection(collection).document().set(data)
    # print("[Success] SetDB")

# targetフォルダの中にある画像のパスを取得
def listup_image(folder, path_list):
    patternStr = '.+\.(jpg|png)'
    pattern = re.compile(patternStr)
    for item in os.listdir(folder):
        result = pattern.match(item)
        # resultが None以外＝画像 なので，パスをリストに追加
        if result:
            path_list.append(folder + '/' + item)
    # print("以下の画像パスをリストに追加しました")
    # for item in path_list:
        # print(f"パスをリストに追加しました:{item}")
    # print("[Success] listup_image")
    return path_list



'''----------------------------------------------------------------
Storageの処理
----------------------------------------------------------------'''
# 画像をStorageにアップロード
def upload_blob(source_file_path, destination_blob_name):
    filename = os.path.basename(source_file_path)
    blob = bucket.blob(destination_blob_name + filename)
    blob.upload_from_filename(source_file_path)
    print(f"destination_blob_name: {destination_blob_name}")
    print(f"filename: {filename}),  get_signed_url: {get_signed_url(destination_blob_name, filename)}")
    return get_signed_url(destination_blob_name, filename)

def get_signed_url(blob_name, filename):
    # return "https://storage.googleapis.com/sahasra-image.appspot.com/" + blob_name + filename
    return "https://storage.googleapis.com/sahasura-5f7bd.appspot.com/" + blob_name + filename



'''----------------------------------------------------------------
分類後フォルダ（特徴量分類・色分類）の処理
----------------------------------------------------------------'''
# classesの要素取得
def get_classification(classification_folder, filename):
    class_list = []
    for i in os.listdir(classification_folder):
        filepath = classification_folder + i + "/" + filename
        if(os.path.exists(filepath)):
            class_list.append(i)
    return class_list


if __name__ == "__main__":
    '''---画像のソースフォルダとアップロード先フォルダ---'''
    img_up_folder = "./imgs/img"  # 画像たちが存在するフォルダ
    obj_up_folder = "./imgs/obj_img"
    img_path_list = []  # 画像のパスを保存するリスト
    obj_path_list = []
    img_target_folder = "oka_img/"  # アップロードする場所(Storage上)
    obj_target_folder = "oka_obj/"

    #   使用する2つのカメラ番号
    cameraID_0 = 2
    cameraID_1 = 3

    class_classification_folder = "./classes/"  # 特徴量分類済みフォルダ
    color_classification_folder = "./colors/"   # 色分類済みフォルダ
    '''-----------------------------------------'''

    '''--------データベース設定--------'''
    collection = u"oka_object"
    users = u""
    # 登録内容
    cameraID = [cameraID_0, cameraID_1]
    classes = []
    colors = []
    images = u""
    objectImages = u""
    projectID = u"oka_TestProject"
    sDatetime = datetime.datetime.now()
    sTimestamp = datetime.datetime.now()
    timestamp = datetime.datetime.now()
    state = 1
    x = 0
    x0 = 0
    x1 = 0
    y = 0
    y0 = 0
    y1 = 0
    z = 0
    '''------------------------------'''

    # Firebaseのイニシャライズ
    FirebaseInitialize()

    # 画像たちのパスをリストに保存
    img_path_list = listup_image(img_up_folder, img_path_list)
    filenum_count = 0
    for path in os.listdir(img_up_folder):
        filenum_count += 1
    for i in range(int(filenum_count/2)):
        img_camera1 = str(i) + "-" + str(cameraID_0) + ".jpg"
        img_camera2 = str(i) + "-" + str(cameraID_1) + ".jpg"
        images1_path = img_up_folder + "/" + img_camera1
        images2_path = img_up_folder + "/" + img_camera2
        print(f"images1_path {images1_path},  img_target_folder {img_target_folder}")
        print(f"images2_path {images2_path},  img_target_folder {img_target_folder}")
        print(f"---{img_camera1} と {img_camera2}------------------------------------------------")
        images1 = upload_blob(images1_path, img_target_folder)
        images2 = upload_blob(images2_path, img_target_folder)
        images_list = []
        classes = []
        colors = []
        images_list.append(images1)
        images_list.append(images2)
        # カメラ１とカメラ２の画像が揃っているかを確認し，対応するobject画像を探す．
        if os.path.isfile(img_up_folder + "/" + img_camera1):
            if os.path.isfile(img_up_folder + "/" + img_camera2):
                # print("カメラ１・カメラ２の画像は正常に存在しています")
                glob_path = obj_up_folder + "/obj-" + str(i) + "-*"
                globfiles = glob.glob(glob_path)
                obj_img_list = []
                classes = []
                colors = []
                for name in globfiles:
                    no_of_cam = int(name[-5])

                    # どの分類フォルダに属しているか（classes と colors の入力）
                    classes.extend(get_classification(class_classification_folder, os.path.basename(name)))
                    colors.extend(get_classification(color_classification_folder, os.path.basename(name)))
                    classes = list(set(classes))
                    colors = list(set(colors))
                    if no_of_cam == cameraID_0:
                        # print(name, obj_target_folder)
                        obj_img_list.append(upload_blob(name, obj_target_folder))
                    elif no_of_cam == cameraID_1:
                        # print(name, obj_target_folder)
                        obj_img_list.append(upload_blob(name, obj_target_folder))
                    else:
                        print(f"カメラ番号不明")
                SetDB(collection, users, cameraID, classes, colors, images_list, obj_img_list, projectID, sDatetime, sTimestamp, state, timestamp, x, x0, x1, y, y0, y1, z)
            else:
                print("カメラ２の画像がありません")
        else:
            print("カメラ１orカメラ２の画像がありません")