import cv2
import time

img=cv2.imread("./field.png")
cv2.imshow("my window",img)

while True:
    cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
    print("hel")
    cv2.imshow("my window",img)
    time.sleep(0.1)