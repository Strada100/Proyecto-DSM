import numpy as np
#Estos rangos son de las caras digitales.
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
    """
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
    """
        #El array toma valores de HSV ---> H=Matiz (0 a 179)   S=Saturacion (0 a 255)  V=Brillo  (0 a 255)
    RedBajo1=np.array([170, 100, 100], np.uint8)
    RedAlto1=np.array([179, 255, 255], np.uint8)
    RedBajo2=np.array([0, 155, 150], np.uint8)
    RedAlto2=np.array([5, 255, 255], np.uint8)
    R2_rojo=[RedBajo1,RedAlto1,RedBajo2,RedAlto2]
    #Azul
    BlueBajo=np.array([100,175,200],np.uint8)
    BlueAlto=np.array([120,255,255],np.uint8)
    R_azul=[BlueBajo,BlueAlto]
    #Amarillo
    YellowBajo=np.array([25,100,120],np.uint8)
    YellowAlto=np.array([45,255,255],np.uint8)
    R_amarillo=[YellowBajo,YellowAlto]
    #Verde
    GreenBajo=np.array([50,100,100],np.uint8)
    GreenAlto=np.array([80,255,255],np.uint8)
    R_verde=[GreenBajo,GreenAlto]
    #Naranja
    OrangeBajo=np.array([6,200,20],np.uint8)
    OrangeAlto=np.array([24,255,255],np.uint8)
    R_naranja=[OrangeBajo,OrangeAlto]
    #Blanco
    WhiteBajo=np.array([0,0,0],np.uint8)
    WhiteAlto=np.array([180,10,10],np.uint8)
    R_blanco=[WhiteBajo,WhiteAlto]
    return R2_rojo,R_azul,R_naranja,R_verde, R_amarillo, R_blanco


#Estos colores son los de los puntos, se hicieron manual.
#Esto para grabar los colores en codigo HSV en un excel y hacer despues un agente que me pueda predecir el color.
def colores_finales():
    # "Rojo"   "Naranja"     "Azul"     "Amarillo"      "Verde"       "Blanco"
    
    #C_back=["","Rojo","Rojo","Amarillo","Amarillo","Blanco","Azul","Verde","Verde","Blanco"]
    #C_bottom=["","Naranja" ,"Naranja" ,"Azul","Amarillo" ,"Verde" ,"Rojo","Amarillo" ,"Azul","Azul"]
    #C_front=["","Rojo", "Verde","Azul","Azul","Amarillo","Blanco","Blanco","Naranja","Rojo"]
    #C_left=["","Verde", "Rojo", "Amarillo", "Blanco","Rojo", "Amarillo", "Naranja", "Azul", "Rojo"]
    #C_right=["","Amarillo" , "Rojo", "Verde", "Naranja", "Naranja", "Naranja", "Azul", "Verde", "Blanco"]
    #C_top=["","Naranja", "Verde", "Blanco", "Amarillo", "Azul", "Blanco", "Verde", "Blanco", "Naranja"]
    """
    #Test6 - Fotos de Alex
    C_back=["","Blanco","Blanco","Naranja","Verde","Amarillo","Azul","Rojo","Amarillo","Rojo"]
    C_bottom=["","Blanco" ,"Naranja" ,"Amarillo","Amarillo" ,"Verde" ,"Verde","Rojo" ,"Naranja","Blanco"]
    C_front=["","Verde", "Azul","Azul","Verde","Azul","Azul","Blanco","Blanco","Verde"]
    C_left=["","Naranja", "Rojo", "Amarillo", "Naranja","Blanco", "Naranja", "Azul", "Amarillo", "Naranja"]
    C_right=["","Verde" , "Rojo", "Amarillo", "Rojo", "Rojo", "Blanco", "Rojo", "Azul", "Verde"]
    C_top=["","Amarillo", "Blanco", "Azul", "Rojo", "Naranja", "Amarillo", "Naranja", "Verde", "Azul"]
    
    #Test7 - Fotos de JS
    C_back=["","Azul","Amarillo","Amarillo","Naranja","Verde","Rojo","Azul","Naranja","Blanco"]
    C_bottom=["","Amarillo" ,"Amarillo" ,"Blanco","Verde" ,"Azul" ,"Verde","Blanco" ,"Rojo","Amarillo"]
    C_front=["","Rojo", "Blanco","Rojo","Rojo","Rojo","Blanco","Naranja","Naranja","Verde"]
    C_left=["","Azul", "Azul", "Blanco", "Naranja","Amarillo", "Azul", "Verde", "Blanco", "Verde"]
    C_right=["","Naranja" , "Verde", "Naranja", "Amarillo", "Naranja", "Azul", "Verde", "Blanco", "Naranja"]
    C_top=["","Amarillo", "Amarillo", "Azul", "Azul", "Blanco", "Rojo", "Rojo", "Verde", "Rojo"]
    """
    #Test8 - Fotos de Angel lotelo
    C_back="Naranja"
    C_bottom="Amarillo"
    C_front="Rojo"
    C_left="Verde"
    C_right="Azul"
    C_top="Blanco"
    """
    #Test9 - Fotos cubo renovado
    C_back=["","Naranja","Azul","Amarillo","Naranja","Azul","Azul","Verde","Naranja","Rojo"]
    C_bottom=["","Amarillo" ,"Blanco" ,"Verde","Rojo" ,"Amarillo" ,"Rojo","Verde" ,"Verde","Verde"]
    C_front=["","Azul", "Azul","Rojo","Amarillo","Verde","Verde","Blanco","Naranja","Blanco"]
    C_left=["","Amarillo", "Blanco", "Naranja", "Blanco","Naranja", "Verde", "Naranja", "Verde", "Amarillo"]
    C_right=["","Azul" , "Amarillo", "Naranja", "Amarillo", "Rojo", "Azul", "Azul", "Rojo", "Rojo"]
    C_top=["","Azul", "Amarillo", "Blanco", "Blanco", "Blanco", "Rojo", "Rojo", "Naranja", "Blanco"]
    """ 
    #['top', 'bottom', 'left', 'right', 'front', 'back']
    return C_top, C_bottom, C_left, C_right,C_front,C_back 