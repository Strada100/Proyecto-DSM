from cv2 import cv2
import numpy as np
import configuracion
ncara=configuracion.nombre_caras()
#p1, p2, p3, p4, pc, p6, p7, p8, p9
k=0
cap = cv2.VideoCapture(0)
"""
while True:
    ret,frame = cap.read()
    if ret==True:
        cv2.imshow("Foto de la cara "+ncara[k],frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            img_name="Foto_cara_"+ncara[k]+'.jpg'
            cv2.imwrite(img_name, frame)
            print("Foto_cara_"+ncara[k]+' ha sido capturada')
            k=k+1
        if k==6:
            k=0
            break
cap.release()
cv2.destroyAllWindows()

#El array toma valores de HSV ---> H=Matiz (0 a 179)   S=Saturacion (0 a 255)  V=Brillo  (0 a 255)
RedBajo1=np.array([161, 155, 150], np.uint8)
RedAlto1=np.array([180, 255, 255], np.uint8)
RedBajo2=np.array([0, 155, 150], np.uint8)
RedAlto2=np.array([5, 255, 255], np.uint8)
#Azul
BlueBajo=np.array([110,175,200],np.uint8)
BlueAlto=np.array([120,255,255],np.uint8)
#Amarillo
YellowBajo=np.array([20,100,120],np.uint8)
YellowAlto=np.array([45,255,255],np.uint8)
#Verde
GreenBajo=np.array([50,200,200],np.uint8)
GreenAlto=np.array([65,255,255],np.uint8)
#Naranja
OrangeBajo=np.array([10,200,20],np.uint8)
OrangeAlto=np.array([20,255,255],np.uint8)
#Blanco
WhiteBajo=np.array([0,0,0],np.uint8)
WhiteAlto=np.array([180,10,180],np.uint8)
"""
"""
for k in range(len(ncara)):
    image=cv2.imread('foto_cara_'+ncara[k]+'.jpg')
    print('image.shape=',image.shape)
    imageOut=image[50:280,250:500]
    cv2.imshow('Imagen de entrada',image)
    cv2.imshow('Imagen de salida',imageOut)
    img_name="Foto_cara_"+ncara[k]+'.jpg'
    cv2.imwrite(img_name, imageOut)
    print("Foto_cara_"+ncara[k]+' ha sido recortada')
    k=k+1
    cv2.waitKey(0)
cv2.destroyAllWindows()
"""
RedBajo1=np.array([161, 155, 150], np.uint8)
RedAlto1=np.array([180, 255, 255], np.uint8)
RedBajo2=np.array([0, 155, 150], np.uint8)
RedAlto2=np.array([5, 255, 255], np.uint8)
#Azul
BlueBajo=np.array([110,175,200],np.uint8)
BlueAlto=np.array([120,255,255],np.uint8)
#Amarillo
YellowBajo=np.array([20,100,140],np.uint8)
YellowAlto=np.array([45,255,255],np.uint8)
#Verde
GreenBajo=np.array([50,200,200],np.uint8)
GreenAlto=np.array([65,255,255],np.uint8)
#Naranja
OrangeBajo=np.array([6,240,226],np.uint8)
OrangeAlto=np.array([20,255,255],np.uint8)
#Blanco
WhiteBajo=np.array([0,0,229],np.uint8)
WhiteAlto=np.array([180,50,255],np.uint8)




#frame_threshed = cv2.inRange(hsv_img, OrangeBajo, OrangeAlto)
image=cv2.imread('foto_cara_'+ncara[0]+'.jpg')
frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#grises=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#_,maskWhite=cv2.threshold(grises,220,255,cv2.THRESH_BINARY)
maskRed1 = cv2.inRange(frameHSV, RedBajo1, RedAlto1)
maskRed2 = cv2.inRange(frameHSV, RedBajo2, RedAlto2)
maskRed = cv2.add(maskRed1, maskRed2)
maskBlue = cv2.inRange(frameHSV, BlueBajo, BlueAlto)
maskOrange = cv2.inRange(frameHSV, OrangeBajo, OrangeAlto)
maskGreen = cv2.inRange(frameHSV, GreenBajo, GreenAlto)
maskYellow = cv2.inRange(frameHSV, YellowBajo, YellowAlto)
maskWhite=cv2.inRange(frameHSV, WhiteBajo, WhiteAlto)

cv2.imshow('frame', image)
cv2.imshow('Azul', maskBlue)
cv2.imshow('Verde', maskGreen)
cv2.imshow('Roja', maskRed)
cv2.imshow('Amarilla', maskYellow)
cv2.imshow('Naranja', maskOrange)
cv2.imshow('Blanca', maskWhite)

cv2.waitKey(0) 
cap.release()
cv2.destroyAllWindows()