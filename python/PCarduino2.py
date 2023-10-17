import serial
import time

import urllib.request as req
import json

# JSONをダウンロード
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
filename = 'tenki.json'
req.urlretrieve(url, filename)

with open('tenki.json', 'r', encoding="UTF-8") as f:
  data = json.load(f)

nagoya_data = data[11]
nagoya_tomorrow_temps = nagoya_data["srf"]["timeSeries"][2]["areas"]["temps"]
print(nagoya_tomorrow_temps) # 明日の名古屋の[最低気温, 最高気温]


ser =serial.Serial("COM3", 9600)
time.sleep(2)
val = nagoya_tomorrow_temps[1] # 明日の名古屋の最高気温
a = val + 'a'
ser.write(bytes(a,'utf-8'))
ser.close()