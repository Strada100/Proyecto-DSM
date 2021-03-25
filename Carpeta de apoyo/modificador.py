from cv2  import cv2
import numpy as np
import configuracion
ncara=configuracion.nombre_caras()
rangex, rangey, rangex1, rangex2, rangex3, rangey1, rangey2, rangey3=configuracion.rangos()
Azul, Verde, Rojo, Naranja,Amarillo, Blanco=configuracion.colores_basic()
#p1, p2, p3, p4, pc, p6, p7, p8, p9=
for i in range(len(ncara)):
    cara = cv2.imread('Caras digitalizadas\Cara_'+ncara[i]+'.jpg')
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
    cv2.imshow('Cara_'+ ncara[i],cara)
    cv2.imwrite('Cara_'+ ncara[i]+'.jpg', cara)
cv2.waitKey(0)
cv2.destroyAllWindows()