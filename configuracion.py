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
    Blanco=[255,255,255]
    Azul=[255,0,0]
    Verde=[0,255,0]
    Rojo=[0,0,255]
    Naranja=[0,128,255]
    Amarillo=[0,233,255]
    return Blanco, Azul, Verde, Rojo, Amarillo, Naranja