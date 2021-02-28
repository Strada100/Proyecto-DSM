from cv2 import cv2
import numpy as np
import configuracion
ncara=configuracion.nombre_caras()

for p in range(0,6):
    image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[p]+'.jpg')
    ranx=image.shape[1]
    rany=image.shape[0]
    pre_scaler=3
    cv2.imshow('Imagen de entrada',image)

    """
                                        A       B       C       D
                                    A_|_______|_______|_______|
    A=0                               |       |       |       |
    B=ranx//3                         |   P1  |   P2  |   P3  |
    C=2*ranx//3                     E_|_______|_______|_______|
    D=ranx                            |       |       |       |
    E=rany//3                         |   P4  |   P5  |   P6  |
    F=2*rany//3                     F_|_______|_______|_______|
    G=rany                            |       |       |       |
                                      |   P7  |   P8  |   P9  |
                                    G_|_______|_______|_______|
    Tomando en cuenta la primera fila
                P=image[:(1*rany)//3,(n*ranx)//3:(i*ranx)//3]
                P=image[A:E,A:B]
    la "n" nos deja poner cero en el primer rango, y ser a su vez el limitador para el siguiente rango
    n=0 i=1
                P=image[:(1*rany)//3,(n*ranx)//3:(i*ranx)//3]
                P=image[:(1*rany)//3,0:(1*ranx)//3]
                P=image[A:E,A:B]
    incrementan ambos valores 
    n=1 i=2
                P=image[:(1*rany)//3,(n*ranx)//3:(i*ranx)//3]
                P=image[:(1*rany)//3,(1*ranx)//3:(2*ranx)//3]
                P=image[A:E,B:C] 
    incrementan ambos valores 
    n=2 i=3
                P=image[:(1*rany)//3,(n*ranx)//3:(i*ranx)//3]
                P=image[:(1*rany)//3,(2*ranx)//3:(3*ranx)//3]
                P=image[A:E,C:D] 
    Funcion genral
                    P=image[(l*rany)//3:(s*rany)//3,(n*ranx)//3:(i*ranx)//3]

    """
    n=0 #Incrementar el valor para tomar en cuenta el punto anterior en el eje horizontal
    l=0 #Incrementar el valor para tomar en cuenta el punto anterior en el eje vertical
    k=1#numero del punto
    for s in range(1,4): #Cambia de fila
        for i  in range(1,4): #Cambia de columna
            P=image[(l*rany)//3:(s*rany)//3,(n*ranx)//3:(i*ranx)//3]
            Pname='Fotos_caras\Puntos\cara_'+ncara[p]+'\C_'+ncara[p]+'_P_'+str(k)+'.jpg'
            
            cv2.imwrite(Pname,P)
            n=n+1
            
            width=int(P.shape[1]*pre_scaler)
            heigth=int(P.shape[0]*pre_scaler)
            dimension=(width,heigth)
            pp=cv2.imread(Pname)
            Punto=cv2.resize(pp,dimension,interpolation=cv2.INTER_AREA)
            cv2.imwrite(Pname,P)
            #cv2.imshow('Punto '+str(k),Punto)
            k=k+1
        n=0
        l=l+1   
    #cv2.destroyAllWindows()