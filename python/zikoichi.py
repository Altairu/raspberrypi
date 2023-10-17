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
field_width = 3462  # フィールドの幅 (mm)
field_height = 7000  # フィールドの高さ (mm)

# フィールド写真のサイズ
img_width = 637  # フィールド写真の幅 (ピクセル)
img_height = 1267  # フィールド写真の高さ (ピクセル)

# 画像の表示
plt.figure(figsize=(img_width / 100, img_height / 100))  # グラフのサイズを指定 (ピクセルをcmに変換)
plt.imshow(field_img, extent=[0, field_width, 0, field_height])

while True:
    data = ser.readline().decode().strip()
    if data.startswith("(") and data.endswith(")"):
        data = data[1:-1]
        y, x, _ = map(int, data.split(", "))  # y を縦軸、x を横軸として受信

        # ロボットの座標データをフィールドの寸法に合わせて変換
        x = x * field_width / img_width
        y = y * field_height / img_height

        x_positions.append(x)
        y_positions.append(y)

        # プロットの更新
        plt.scatter(y_positions, x_positions, c='r', marker='o')
        plt.pause(0.01)

plt.show()
