from cv2 import cv2
import numpy as np
Green=np.uint8([[[0,255,0]]])
Orange=np.uint8([[[0,128,255]]])
White=np.uint8([[[1,255,255]]])

hsv_green=cv2.cvtColor(Green,cv2.COLOR_BGR2HSV)
hsv_orange=cv2.cvtColor(Orange,cv2.COLOR_BGR2HSV)
hsv_white=cv2.cvtColor(White,cv2.COLOR_BGR2HSV)
print(hsv_green)
print(hsv_orange)
print(hsv_white)