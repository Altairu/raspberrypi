import serial
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# フィールド写真の読み込み
field_img = mpimg.imread('field.png')

# プロット用のリスト
x_positions = []
y_positions = []

# シリアル通信の設定
ser = serial.Serial('/dev/ttyACM0', 115200)

# フィールドの寸法
field_width = 7000  # フィールドの幅 (mm)
field_height = 3462  # フィールドの高さ (mm)

# 画像の表示
plt.imshow(field_img, extent=[0, field_height, 0, field_width])

while True:
    data = ser.readline().decode().strip()
    if data.startswith("(") and data.endswith(")"):
        data = data[1:-1]
        y, x, _ = map(int, data.split(", "))  # y を縦軸、x を横軸として受信

        # ロボットの座標データをフィールドの寸法に合わせて変換
        x = x * field_width / 637
        y = y * field_height / 1267

        x_positions.append(x)
        y_positions.append(y)

        # プロットの更新
        plt.scatter(y_positions, x_positions, c='r', marker='o')
        plt.pause(0.01)

plt.show()
