from cv2 import cv2
import numpy as np
import configuracion
import Agente
import pandas as pd
import openpyxl 
ncara=configuracion.nombre_caras()
Azul, Verde, Rojo, Naranja,Amarillo, Blanco=configuracion.colores_basic()
rangex, rangey, rangex1, rangex2, rangex3, rangey1, rangey2, rangey3=configuracion.rangos()
Colores_puntos=[""]
Abre_caras=configuracion.Abre_caras()

def hacer_caras():
    cara = np.ones((rangex,rangey),dtype=np.uint8)
    #Son los 9 cuadrados de la cara
    #Primera fila
    cara[:rangex1,:rangey1] = 125
    cara[:rangex1,rangey1:rangey2] = 125
    cara[:rangex1,rangey2:rangey3] = 125
    #Segunda fila
    cara[rangex1:rangex2,:rangey1] = 125
    cara[rangex1:rangex2,rangey1:rangey2] = 125#Este es el punto central
    cara[rangex1:rangex2,rangey2:rangey3] = 125
    #Tercera fila
    cara[rangex2:rangex3,:rangey1] = 125
    cara[rangex2:rangex3,rangey1:rangey2] = 125
    cara[rangex2:rangex3,rangey2:rangey3] = 125
    for i in range(len(ncara)):
        cv2.imwrite('Caras digitalizadas\Cara_'+ ncara[i]+'.jpg', cara)


def modificar_caras(cara, npunto, color):
    #Abre la cara digital
    face = cv2.imread('Caras digitalizadas\Cara_'+cara+'.jpg')
    font = cv2.FONT_HERSHEY_SIMPLEX
    
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
        cv2.putText(face,Abre_caras[ncara.index(cara)],(65,85),font,1,(0,0,0),2,cv2.LINE_AA)
        #cv2.putText(imagen,'Practicando con OpenCV',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)
        #cv2.putText(face,Abre_caras[ncara.index(cara)], ((rangex1+rangex2)/2,(rangey1+rangey2)/2), 2, 255)
    elif npunto==6:
        face[rangex1:rangex2,rangey2:rangey3] = color
    elif npunto==7:
        face[rangex2:rangex3,:rangey1] =color
    elif npunto==8:
        face[rangex2:rangex3,rangey1:rangey2] =color
    elif npunto==9:
        face[rangex2:rangex3,rangey2:rangey3] = color
    #Guarda la cara diital
    cv2.imwrite('Caras digitalizadas\Cara_'+ cara+'.jpg', face)

    

def toma_fotos():
    k=0
    cap = cv2.VideoCapture(0)
    
    #El siguiente ciclo me permite tomar las fotos de las caras.
    #Al oprimir la tecla espacio se tomara la foto y en la terminal aparecerá el mensaje
    #La foto se guardara con el nombre de la cara

    while True:
        ret,frame = cap.read()
        
        if ret==True:
            cv2.rectangle(frame,(200,100),(500,400),(0,0,255),3)
            cv2.imshow("Foto de la cara "+ncara[k],frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                img_name="Fotos_caras\Foto_cara_"+ncara[k]+'.jpg'
                cv2.imwrite(img_name, frame)
                print("Foto_cara_"+ncara[k]+' ha sido capturada')
                k=k+1
            if k==6:
                k=0
                break
    cap.release()
    cv2.destroyAllWindows()

#toma_fotos()
def recorta_fotos():
    k=0
    #El siguiente ciclo es para recortar las imagenes y que solo salga la cara del cubo
    #capitulo8
    for k in range(len(ncara)):
        #Abrir la foto tomada
        image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[k]+'.jpg')
        #Recortar el marco donde se tomo la foto
        imageOut=image[100:400,200:500]
        img_name="Fotos_caras\Foto_cara_"+ncara[k]+'.jpg'
        cv2.imwrite(img_name, imageOut)
        #print("Foto_cara_"+ncara[k]+' ha sido recortada')
        k=k+1

#recorta_fotos()
def recortar_puntos():
    for p in range(0,6):
        image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[p]+'.jpg')
        #image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[p]+'.jpeg')
        ranx=image.shape[1]
        rany=image.shape[0]
        pre_scaler=5
        #cv2.imshow('Imagen de entrada',image)

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
                P=image[(l*rany+3)//3:(s*rany-3)//3,(n*ranx+3)//3:(i*ranx-3)//3]
                Pname='Fotos_caras\Puntos\cara_'+ncara[p]+'\C_'+ncara[p]+'_P_'+str(k)+'.jpg'
                
                cv2.imwrite(Pname,P)
                n=n+1
                
                width=int(P.shape[1]*pre_scaler)
                heigth=int(P.shape[0]*pre_scaler)
                dimension=(width,heigth)
                pp=cv2.imread(Pname)
                Punto=cv2.resize(pp,dimension,interpolation=cv2.INTER_AREA)
                cv2.imwrite(Pname,Punto)
                #cv2.imshow('Punto '+str(k),Punto)
                k=k+1
            n=0
            l=l+1   
        #cv2.destroyAllWindows()
#recortar_puntos()
"""
Este es el formato en el que se va a trabajar. Las letras corresponde a la cara.

             |************|
             |*U1**U2**U3*|
             |************|
             |*U4**U5**U6*|
             |************|
             |*U7**U8**U9*|
             |************|
 ************|************|************|************
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 ************|************|************|************
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 ************|************|************|************
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 ************|************|************|************
             |************|
             |*D1**D2**D3*|
             |************|
             |*D4**D5**D6*|
             |************|
             |*D7**D8**D9*|
             |************|
"""

def Pintar_caras():
    for c in range(0,6):
            cara=ncara[c]
            for npunto in range(1,10):
                punto=cv2.imread('Fotos_caras\Puntos\cara_'+ncara[c]+'\C_'+ncara[c]+'_P_'+str(npunto)+'.jpg')
                #Se va a leer el color más frecuente de la imagen para compararlo con alguno de la base de datos 
                colors, count = np.unique(punto.reshape(-1, punto.shape[-1]), axis=0, return_counts=True)
                Primer_color=colors[np.argsort(-count)][:1]
                ArrayBGR=Primer_color[0]
                #Se normalizan los valores de la base de datos
                (DataNorm,MRange)=Agente.NormalData(Agente.DatabaseRead())
                #se manda al Agente para que encuentre una coicidencia, y desnormaliza el resultado para encontrar una coicidencia del 1-6
                #Los cuales, cada uno hace referencia a un color
                r=Agente.Agente(ArrayBGR,DataNorm, MRange) 
                #Matices de la cara digitales
                colores=[Blanco,Amarillo,Azul,Verde,Rojo,Naranja] 
                #Color en formato string
                String_Colores=["Blanco","Amarillo","Azul","Verde","Rojo","Naranja"]
                
                #Se buscara la coicidencia del color del punto con la base, y se procedera a colorear el punto
                find=False
                t=1
                while find==False:
                    if t==r:
                        modificar_caras(cara,npunto,colores[t-1])
                        #Se va a hacer una lista de 55 elementos, sonde el primero no va a contar.
                        #Cada p colores serán los correspondientes cada cara.
                        Colores_puntos.append(String_Colores[t-1])
                        find=True
                    elif t>=7:
                        find=True #Solo es para salir del bucle while en caso de no encontrar 
                    else:
                        t=t+1
    return Colores_puntos

#Pintar_caras()
