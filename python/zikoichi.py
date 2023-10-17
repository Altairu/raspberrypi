import serial
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# フィールド写真の読み込み
field_img = mpimg.imread('field.png')

# シリアル通信の設定
ser = serial.Serial('/dev/ttyACM3', 115200)

# フィールドの寸法
field_width = 3462  # フィールドの幅 (mm)
field_height = 7000  # フィールドの高さ (mm)

# フィールド写真のサイズ
img_width = 637  # フィールド写真の幅 (ピクセル)
img_height = 1267  # フィールド写真の高さ (ピクセル)

# 画像の表示
plt.figure(figsize=(img_width / 100, img_height / 100))  # グラフのサイズを指定 (ピクセルをcmに変換)
plt.imshow(field_img, extent=[0, field_width, 0, field_height])

arrow = plt.arrow(0, 0, 0, 0, head_width=50, head_length=100, fc='g', ec='g')
plt.xlim(0, field_width)
plt.ylim(0, field_height)

first_data_received = False

while True:
    data = ser.readline().decode().strip()
    if data.startswith("(") and data.endswith(")"):
        data = data[1:-1]
        y, x, theta = map(int, data.split(", "))  # y を縦軸、x を横軸、theta を角度として受信

        # ロボットの座標データをフィールドの寸法に合わせて変換
        x = x 
        y = y 

        # ロボットの向きを示す矢印を更新
        arrow.remove()
        arrow = plt.arrow(x, y, 100 * np.cos(np.deg2rad(theta)), 100 * np.sin(np.deg2rad(theta)),
                          head_width=50, head_length=100, fc='g', ec='g')

        plt.pause(0.01)

        if not first_data_received:
            first_data_received = True

# グラフを閉じる
plt.close()
