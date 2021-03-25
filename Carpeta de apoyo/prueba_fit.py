from cv2 import cv2
import numpy as np
import configuracion
import caras
import pandas as pd
import openpyxl 
ncara=configuracion.nombre_caras()
#Mando a llamar del archivo configuracion los matices a detectar
R2_rojo,R_azul,R_naranja,R_verde, R_amarillo, R_blanco=configuracion.matices()
Azul, Verde, Rojo, Naranja,Amarillo, Blanco=configuracion.colores_basic()
""""
cap = cv2.VideoCapture(0)
#p1, p2, p3, p4, pc, p6, p7, p8, p9   

for n in range(1,6):
    image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[n]+'.jpg') #leemos la imagen
    for k in range(1,9):   
        frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, R2_rojo[0], R2_rojo[1])
        maskRed2 = cv2.inRange(frameHSV, R2_rojo[2], R2_rojo[3])
        maskRed = cv2.add(maskRed1, maskRed2) #Como se puede ver en la imagen de HSV, el color rojo se parte
        maskBlue = cv2.inRange(frameHSV, R_azul[0], R_azul[1])
        maskOrange = cv2.inRange(frameHSV, R_naranja[0], R_naranja[1])
        maskGreen = cv2.inRange(frameHSV, R_verde[0], R_verde[1])
        maskYellow = cv2.inRange(frameHSV, R_amarillo[0], R_amarillo[1])

cv2.waitKey(0) 
cap.release()
cv2.destroyAllWindows()
"""



def contorno(mask,color):
  contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    
    if area > 0:
      pintar=True
    else: 
        pintar=False
    return pintar

def fit_colors2():
    for c in range(0,6):
        cara=ncara[c]
        for npunto in range(1,9):
            punto=cv2.imread('Fotos_caras\Puntos\cara_'+ncara[c]+'\C_'+ncara[c]+'_P_'+str(npunto)+'.jpg')
            #cv2.imshow('Imagen de entrada',punto)
            frameHSV = cv2.cvtColor(punto, cv2.COLOR_BGR2HSV)
            maskRed1 = cv2.inRange(frameHSV, R2_rojo[0], R2_rojo[1])
            maskRed2 = cv2.inRange(frameHSV, R2_rojo[2], R2_rojo[3])
            maskRed = cv2.add(maskRed1, maskRed2) #Como se puede ver en la imagen de HSV, el color rojo se parte
            maskBlue = cv2.inRange(frameHSV, R_azul[0], R_azul[1])
            maskOrange = cv2.inRange(frameHSV, R_naranja[0], R_naranja[1])
            maskGreen = cv2.inRange(frameHSV, R_verde[0], R_verde[1])
            maskYellow = cv2.inRange(frameHSV, R_amarillo[0], R_amarillo[1])
            cv2.imshow('Azul',maskBlue)
            cv2.imshow('Verde',maskGreen)
            cv2.imshow('Amarillo',maskYellow)
            cv2.imshow('Rojo',maskRed)
            cv2.imshow('Naranja',maskOrange)
            c_azul=contorno(maskBlue,Azul)
            c_verde=contorno(maskGreen,Verde)
            c_rojo=contorno(maskRed,Rojo)
            c_naranja=contorno(maskOrange,Naranja)
            c_amarillo=contorno(maskYellow,Amarillo)

            color_cuadro=[c_azul,c_naranja,c_rojo,c_verde,c_amarillo]
            colores=[Azul,Naranja,Rojo,Verde,Amarillo]
            for t in range(len(color_cuadro)):
                if color_cuadro[t]==True:
                    caras.modificar_caras(cara,npunto,colores[t])
        
caras.hacer_caras()

        
        


