from cv2  import cv2
import numpy as np
import configuracion
ncara=configuracion.nombre_caras()
rangex, rangey, rangex1, rangex2, rangex3, rangey1, rangey2, rangey3=configuracion.rangos()


def hacer_caras():
    cara = np.ones((rangex,rangey),dtype=np.uint8)
    #Son los 9 cuadrados de la cara
    #Primera fila
    cara[:rangex1,:rangey1] = 0
    cara[:rangex1,rangey1:rangey2] = 0
    cara[:rangex1,rangey2:rangey3] = 0
    #Segunda fila
    cara[rangex1:rangex2,:rangey1] = 0
    cara[rangex1:rangex2,rangey1:rangey2] = 0#Este es el punto central
    cara[rangex1:rangex2,rangey2:rangey3] = 0
    #Tercera fila
    cara[rangex2:rangex3,:rangey1] = 0
    cara[rangex2:rangex3,rangey1:rangey2] = 0
    cara[rangex2:rangex3,rangey2:rangey3] = 0
    for i in range(len(ncara)):
        #cv2.imshow('Cara_'+ ncara[i],cara)
        cv2.imwrite('Caras digitalizadas\Cara_'+ ncara[i]+'.jpg', cara)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

def modificar_caras(cara, npunto, color):
    face = cv2.imread('Caras digitalizadas\Cara_'+cara+'.jpg')
    if npunto==1:
        face[:rangex1,:rangey1] = color
    elif npunto==2:
        face[:rangex1,rangey1:rangey2] = color
    elif npunto==3:
        face[:rangex1,rangey2:rangey3] = color
    elif npunto==4:
        face[rangex1:rangex2,:rangey1] = color
    elif npunto==5:
        face[rangex1:rangex2,rangey1:rangey2] = color#Este es el punto central
    elif npunto==6:
        face[rangex1:rangex2,rangey2:rangey3] = color
    elif npunto==7:
        face[rangex2:rangex3,:rangey1] =color
    elif npunto==8:
        face[rangex2:rangex3,rangey1:rangey2] =color
    elif npunto==9:
        face[rangex2:rangex3,rangey2:rangey3] = color
    
    #cv2.imshow('Cara_'+ cara,face)
    cv2.imwrite('Caras digitalizadas\Cara_'+ cara+'.jpg', face)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    


    
