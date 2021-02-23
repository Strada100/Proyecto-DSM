from cv2  import cv2
import numpy as np
import configuracion
rangex, rangey, rangex1, rangex2, rangex3, rangey1, rangey2, rangey3, ncara=configuracion.rangos()
Blanco, Azul, Verde, Rojo, Amarillo, Naranja=configuracion.colores_basic()

cara = cv2.imread('Cara_top.jpg')

#Son los 9 cuadrados de la cara
#Primera fila
cara[:rangex1,:rangey1] = Azul
cara[:rangex1,rangey1:rangey2] = Rojo
cara[:rangex1,rangey2:rangey3] = Verde
#Segunda fila
cara[rangex1:rangex2,:rangey1] = Naranja
cara[rangex1:rangex2,rangey1:rangey2] = Blanco#Este es el punto central
cara[rangex1:rangex2,rangey2:rangey3] = Amarillo
#Tercera fila
cara[rangex2:rangex3,:rangey1] = Azul
cara[rangex2:rangex3,rangey1:rangey2] = Verde
cara[rangex2:rangex3,rangey2:rangey3] = Rojo
cv2.imshow('Cara_',cara)
cv2.waitKey(0)
cv2.destroyAllWindows()