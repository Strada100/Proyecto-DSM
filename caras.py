from cv2  import cv2
import numpy as np
import configuracion
rangex, rangey, rangex1, rangex2, rangex3, rangey1, rangey2, rangey3, ncara=configuracion.rangos()

cuadrado = np.ones((rangex,rangey),dtype=np.uint8)

#Son los 9 cuadrados de la cara
#Primera fila
cuadrado[:rangex1,:rangey1] = 255
cuadrado[:rangex1,rangey1:rangey2] = 255
cuadrado[:rangex1,rangey2:rangey3] = 255
#Segunda fila
cuadrado[rangex1:rangex2,:rangey1] = 255
cuadrado[rangex1:rangex2,rangey1:rangey2] = 255#Este es el punto central
cuadrado[rangex1:rangex2,rangey2:rangey3] = 255
#Tercera fila
cuadrado[rangex2:rangex3,:rangey1] = 255
cuadrado[rangex2:rangex3,rangey1:rangey2] = 255
cuadrado[rangex2:rangex3,rangey2:rangey3] = 255
for i in range(len(ncara)):
    cv2.imshow('Cara_'+ ncara[i],cuadrado)
    cv2.imwrite('Cara_'+ ncara[i]+'.jpg', cuadrado)
    cv2.waitKey(0)
cv2.destroyAllWindows()