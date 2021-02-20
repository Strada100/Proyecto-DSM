from cv2  import cv2
import numpy as np

cuadrado = np.zeros((600,600),dtype=np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

#Son los 9 cuadrados de la cara
#Primera fila
cuadrado[:200,:200] = 255
cuadrado[:200,200:400] = 0
cuadrado[:200,400:600] = 255
#Segunda fila
cuadrado[200:400,:200] = 0
cuadrado[200:400,200:400] = 125#Este es el punto central
cuadrado[200:400,400:600] = 0
#Tercera fila
cuadrado[400:600,:200] = 255
cuadrado[400:600,200:400] = 0
cuadrado[400:600,400:600] = 255

cv2.imshow('Cara del cubo',cuadrado)
cv2.waitKey(0)
cv2.destroyAllWindows()