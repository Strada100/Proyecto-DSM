from cv2 import cv2
import numpy as np
import configuracion
import detector_caras
import pandas as pd
from openpyxl import Workbook, load_workbook 
ncara=configuracion.nombre_caras()
#La siguiente instruccion contiene unos valores puestos a mano en la configuracion.py
colores_puntos=configuracion.colores_finales()
#La siguiente instruccion contiene los tonos en formato BGR que deberan tener los puntos digitales
Azul, Verde, Rojo, Naranja,Amarillo, Blanco=configuracion.colores_basic()

def SaveBGR():
    wb=load_workbook('Base_Colores.xlsx') #Abrir la base de datos
    ws=wb['Recepcion'] #Abrir la hoja recepcion
    indice=1136  #Actualizar si se va a anexar más informacion a la base de datos
    for c in range(0,6):
        cara=ncara[c]
        for npunto in range(1,10):
            #Abrir la foto del punto a analizar
            punto=cv2.imread('Fotos_caras\Puntos\cara_'+ncara[c]+'\C_'+ncara[c]+'_P_'+str(npunto)+'.jpg') 
            #Reconocer los 5 colores más frecuentes de la imagen
            colors, count = np.unique(punto.reshape(-1, punto.shape[-1]), axis=0, return_counts=True)
            #Guardar los 5 colores en la variable 
            Colores_imagen=colors[np.argsort(-count)][:5]
            for i in range(5): #Separar la info del color detectado en el formato BGR
                B=Colores_imagen[i][0] #Acceder a la componete B del color i
                G=Colores_imagen[i][1]
                R=Colores_imagen[i][2]
                ws['A'+str(indice)]=B #Guardar el valor en la columna correspondiente
                ws['B'+str(indice)]=G
                ws['C'+str(indice)]=R
                ws['F'+str(indice)]=colores_puntos[c]
                indice=indice+1
            wb.save('Base_Colores.xlsx') #guardar la base de datos

#SaveHSV()

