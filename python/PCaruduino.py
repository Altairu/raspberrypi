import serial
import time

ser =serial.Serial("COM19", 9600) # ここのポート番号を変更
time.sleep(2)
val = 30 # ここの値を変更すると、Arduinoの挙動が変わる
a = str(val) + 'a'
ser.write(bytes(a,'utf-8'))
ser.close()