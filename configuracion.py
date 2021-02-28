import numpy as np
def rangos():
    rangex=150
    rangey=150
    rangex1 = int(rangex/3)
    rangex2 = int(2*rangex/3)
    rangex3 = rangex
    rangey1 = int(rangey/3)
    rangey2 = int(2*rangey/3)
    rangey3 = rangey
    
    return rangex, rangey, rangex1, rangex2, rangex3, rangey1, rangey2, rangey3
def nombre_caras():
    ncara=['top', 'bottom', 'left', 'right', 'front', 'back']
    return ncara
def colores_basic():
#colores de caras
    #BGR
    Azul=[255,0,0]
    Verde=[0,255,0]
    Rojo=[0,0,255]
    Naranja=[0,128,255]
    Amarillo=[0,233,255]
    Blanco=[255,255,255]
    return Azul, Verde, Rojo, Naranja,Amarillo, Blanco
def matices():
    #Las siguientes matrices o arrays se usaran como un rango de deteccion de colores.
    #El array toma valores de HSV ---> H=Matiz (0 a 179)   S=Saturacion (0 a 255)  V=Brillo  (0 a 255)
    RedBajo1=np.array([170, 70, 130], np.uint8)
    RedAlto1=np.array([180, 255, 255], np.uint8)
    RedBajo2=np.array([0, 70, 120], np.uint8)
    RedAlto2=np.array([0, 255, 255], np.uint8)
    R2_rojo=[RedBajo1,RedAlto1,RedBajo2,RedAlto2]
    #Naranja
    OrangeBajo=np.array([0,20,40],np.uint8)
    OrangeAlto=np.array([25,255,255],np.uint8)
    R_naranja=[OrangeBajo,OrangeAlto]
    #Amarillo
    YellowBajo=np.array([25,15,15],np.uint8)
    YellowAlto=np.array([40,255,255],np.uint8)
    R_amarillo=[YellowBajo,YellowAlto]
    #Verde
    GreenBajo=np.array([40,50,60],np.uint8)
    GreenAlto=np.array([95,255,255],np.uint8)
    R_verde=[GreenBajo,GreenAlto]
    #Azul
    BlueBajo=np.array([100,80,110],np.uint8)
    BlueAlto=np.array([131,255,255],np.uint8)
    R_azul=[BlueBajo,BlueAlto]
    
    #Blanco
    #El blanco no se siguio usando debido a que el fondo de la cara digitalizada es blanco.
    #Por lo tanto, no es necesario pintarlo, solo cuidaremos de no pintarlo de otro color.
    WhiteBajo=np.array([0,0,239],np.uint8)
    WhiteAlto=np.array([180,20,255],np.uint8)
    R_blanco=[WhiteBajo,WhiteAlto]
    return R2_rojo,R_azul,R_naranja,R_verde, R_amarillo, R_blanco