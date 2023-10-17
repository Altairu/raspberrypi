import serial
import numpy as np
import matplotlib.pyplot as plt

# シリアルポートの設定（必要に応じて変更）
ser = serial.Serial('/dev/ttyACM0', 115200)

# グラフの初期化
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data, 'o', markersize=6)

# 3秒間のデータを保持するためのリングバッファ
max_data_points = 300  # 1秒あたり100データ点 × 3秒
x_ring_buffer = [0] * max_data_points
y_ring_buffer = [0] * max_data_points
current_index = 0

def update_plot(x, y):
    # データをプロット
    x_data.append(x)
    y_data.append(y)
    line.set_data(x_data, y_data)

    # データが3秒分を超えた場合、古いデータを削除
    if len(x_data) > max_data_points:
        x_data.pop(0)
        y_data.pop(0)

    # グラフを更新
    plt.pause(0.01)

while True:
    data = ser.readline().decode().strip()
    if data.startswith("(") and data.endswith(")"):
        data = data[1:-1]
        x, y, _ = map(int, data.split(", "))

        # リアルタイムプロットを更新
        update_plot(x, y)
