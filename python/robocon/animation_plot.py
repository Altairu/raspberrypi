import matplotlib.pyplot as plt
import serial
import matplotlib.image as mpimg
import matplotlib.animation as animation
import numpy as np

# フィールド写真の読み込み
field_img = mpimg.imread('field.png')

# シリアル通信の設定
ser = serial.Serial('/dev/ttyACM0', 115200)

fig, ax = plt.subplots()

# フィールドの寸法
field_width = 3462  # フィールドの幅 (mm)
field_height = 7000  # フィールドの高さ (mm)

# フィールド写真のサイズ
img_width = 637  # フィールド写真の幅 (ピクセル)
img_height = 1267  # フィールド写真の高さ (ピクセル)

x_positions = []
y_positions = []
thetas = []

ax.imshow(field_img, extent=[0, field_width, 0, field_height])

# # ロボットの向きを示す矢印
arrow = None

while True:
    data = ser.readline().decode().strip()
    if data.startswith("(") and data.endswith(")"):
        data=data[1:-1]
        y, x, theta = map(int, data.split(", "))  # y を縦軸、x を横軸、theta を角度として受信
        x_positions.append(x)
        y_positions.append(y)
        thetas.append(theta)
        ax.cla() 

		# プロットの更新
        ax.scatter(y_positions, x_positions, c='r', marker='o')

		# ロボットの向きを示す矢印を描画
        if len(x_positions) > 0:
            current_x, current_y = x_positions[-1], y_positions[-1]
            arrow_length = 100
            dx = arrow_length * np.cos(np.deg2rad(theta))
            dy = arrow_length * np.sin(np.deg2rad(theta))
            if arrow is not None:
                    arrow.remove()
            ax.imshow(field_img, extent=[0, field_width, 0, field_height])
            arrow = ax.arrow(current_y, current_x, dy, dx, head_width=50, head_length=50, fc='g', ec='g')
        plt.pause(0.01)

