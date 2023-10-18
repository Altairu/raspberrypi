import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import time

# シリアルポートの設定（必要に応じて変更）
ser = serial.Serial('/dev/ttyACM1', 115200)

# グラフの初期化
fig, ax = plt.subplots()
x_data, y_data, theta_data, timestamps = [], [], [], []
line = None

# X軸およびY軸の範囲を設定
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)

def update_plot(x, y, theta, timestamp):
    x_data.append(x)
    y_data.append(y)
    theta_data.append(theta)
    timestamps.append(timestamp)

    # グラフをクリア
    ax.clear()

    # 直線を描画
    if len(x_data) > 1:
        line = Line2D(x_data[-2:], y_data[-2:], linewidth=50, color='blue')
        ax.add_line(line)

    # データ点をプロット
    ax.plot(x_data, y_data, 'o', markersize=6)

    # タイムスタンプから3秒以上経過したデータを削除
    current_time = time.time()
    while timestamps and current_time - timestamps[0] > 3:
        x_data.pop(0)
        y_data.pop(0)
        theta_data.pop(0)
        timestamps.pop(0)

    # グラフの軸範囲を自動調整
    ax.relim()
    ax.autoscale_view()

while True:
    data = ser.readline().decode().strip()
    if data.startswith("(") and data.endswith(")"):
        data = data[1:-1]
        x, y, theta = map(int, data.split(", "))

        # 角度（θ）を度からラジアンに変換
        theta_deg = theta
        theta_rad = np.deg2rad(theta_deg)

        # タイムスタンプを取得
        timestamp = time.time()

        # リアルタイムプロットを更新
        update_plot(x, y, theta_deg, timestamp)

        plt.pause(0.01)
