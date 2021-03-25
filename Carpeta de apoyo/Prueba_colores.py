from cv2 import cv2
import numpy as np
import configuracion
import caras
import Agente
import pandas as pd
import openpyxl 
ncara=configuracion.nombre_caras()
Azul, Verde, Rojo, Naranja,Amarillo, Blanco=configuracion.colores_basic()
def Pintar_caras():
    for c in range(0,6):
            cara=ncara[c]
            for npunto in range(1,10):
                punto=cv2.imread('Fotos_caras\Puntos\cara_'+ncara[c]+'\C_'+ncara[c]+'_P_'+str(npunto)+'.jpg') 
                frameHSV = cv2.cvtColor(punto, cv2.COLOR_BGR2HSV)
                colors, count = np.unique(punto.reshape(-1, punto.shape[-1]), axis=0, return_counts=True)
                Primer_color=colors[np.argsort(-count)][:1]
                ArrayHSV=Primer_color[0]
                (DataNorm,MRange)=Agente.NormalData(Agente.DatabaseRead())
                r=Agente.Agente(ArrayHSV,DataNorm, MRange) 
                colores=[Blanco,Amarillo,Azul,Verde,Rojo,Naranja]
                
                find=False
                t=1
                while find==False:
                    if t==r:
                        caras.modificar_caras(cara,npunto,colores[t-1])
                        find=True
                    elif t>=7:
                        find=True #Solo es para salir del bucle while en caso de no encontrar 
                    else:
                        t=t+1

Pintar_caras()


