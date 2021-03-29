from cv2 import cv2
import numpy as np
import configuracion
import detector_caras
import base_datos
import Agente
import concatenacion
import pandas as pd
import openpyxl
import time
import kociemba
abre=configuracion.Abre_caras()

#Toma de fotografias, recorte de cara y de puntos

#ncara=['up','right','front', 'down', 'left', 'back']
detector_caras.toma_fotos()
detector_caras.recorta_fotos()
detector_caras.recortar_puntos()

#Mandar los nuevas imagenes a la base de datos. 
#Si ya se va a probar, comentar las 2 siguientes lineas

#base_datos.SaveBGR()
#time.sleep(15)

#¿De qué color es mi punto?
#detector_caras.hacer_caras() #Hacer el lienzo de las imagenes digitales 
#Se pintan las caras y se regresa una lista con los colores de las caras
Colores_puntos=detector_caras.Pintar_caras()
#print(Colores_puntos)

#Hacer el plano 2D de cubo
concatenacion.plano2D()

#Valores dados de la lista
#Colores_puntos=['', 'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Blanco', 'Rojo', 'Verde', 'Rojo', 'Amarillo', 'Verde', 'Verde', 'Naranja', 'Azul', 'Naranja', 'Naranja', 'Naranja', 'Blanco', 'Rojo', 'Azul', 'Azul', 'Amarillo', 'Blanco', 'Verde', 'Amarillo', 'Blanco', 'Blanco', 'Azul', 'Azul', 'Azul', 'Naranja', 'Rojo', 'Amarillo', 'Naranja', 'Verde', 'Amarillo', 'Blanco', 'Azul', 'Blanco', 'Blanco', 'Rojo', 'Rojo', 'Verde', 'Blanco', 'Amarillo', 'Rojo', 'Naranja', 'Azul', 'Rojo', 'Naranja', 'Azul', 'Amarillo', 'Verde', 'Verde', 'Amarillo']

Centros=[]
problem=[]
for i in range(5,56,9):
    Centros.append(Colores_puntos[i])
#print(Centros)

c=0
for punto in range(1,55):
    while Colores_puntos[punto]!=Centros[c]:
        c=c+1
    problem.append(abre[c])
    c=0
problema="".join(problem)
problema=problema[0:]
print("Este es el problema a resolver: "+problema)
solucion=kociemba.solve(problema)
print("Esta es la solucion: "+solucion)



    
