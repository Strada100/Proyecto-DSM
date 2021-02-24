from cv2 import cv2
import numpy as np
p1, p2, p3, p4, pc, p6, p7, p8, p9
#Funcion de dibujar contorno
def dibujar(mask,color):
  contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area < 1000 and area>500:
      nuevoContorno = cv2.convexHull(c)
      cv2.drawContours(frame, [nuevoContorno], 0, color, 3)



cap = cv2.VideoCapture(0)
#El array toma valores de HSV ---> H=Matiz (0 a 179)   S=Saturacion (0 a 255)  V=Brillo  (0 a 255)
RedBajo=np.array([161, 155, 84], np.uint8)
RedAlto=np.array([179, 255, 255], np.uint8)
#Azul
BlueBajo=np.array([94,80,2],np.uint8)
BlueAlto=np.array([126,255,255],np.uint8)
#Amarillo
YellowBajo=np.array([15,100,20],np.uint8)
YellowAlto=np.array([45,255,255],np.uint8)
#Verde
GreenBajo=np.array([25,52,72],np.uint8)
GreenAlto=np.array([102,255,255],np.uint8)
#Naranja
OrangeBajo=np.array([11,100,20],np.uint8)
OrangeAlto=np.array([19,255,255],np.uint8)
#Blanco
WhiteBajo=np.array([70,0,200],np.uint8)
WhiteAlto=np.array([100,20,255],np.uint8)

while True:
  ret,frame = cap.read()
  if ret==True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #grises=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #_,maskWhite=cv2.threshold(grises,220,255,cv2.THRESH_BINARY)
    maskRed = cv2.inRange(frameHSV, RedBajo, RedAlto)
    maskBlue = cv2.inRange(frameHSV, BlueBajo, BlueAlto)
    maskOrange = cv2.inRange(frameHSV, OrangeBajo, OrangeAlto)
    maskGreen = cv2.inRange(frameHSV, GreenBajo, GreenAlto)
    maskYellow = cv2.inRange(frameHSV, YellowBajo, YellowAlto)
    maskWhite=cv2.inRange(frameHSV, WhiteBajo, WhiteAlto)
    dibujar(maskBlue,[255,0,0])
    dibujar(maskGreen,[0,255,0])
    dibujar(maskRed,[0,0,255])
    dibujar(maskOrange,[0,128,255])
    dibujar(maskYellow,[0,255,255])
    dibujar(maskWhite,[255,255,255])
    
    cv2.imshow('frame', frame)
    cv2.imshow('Azul', maskBlue)
    cv2.imshow('Verde', maskGreen)
    cv2.imshow('Roja', maskRed)
    cv2.imshow('Amarilla', maskYellow)
    cv2.imshow('Naranja', maskOrange)
    cv2.imshow('Blanca', maskWhite)

    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()