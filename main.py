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


#Toma de fotografias, recorte de cara y de puntos
detector_caras.toma_fotos()
detector_caras.recorta_fotos()
detector_caras.recortar_puntos()

#Mandar los nuevas imagenes a la base de datos. 
#Si ya se va a probar, comentar las 2 siguientes lineas
#base_datos.SaveHSV()
#time.sleep(15)
#¿De qué color es mi punto?
detector_caras.hacer_caras() #Hacer el lienzo de las imagenes digitales 
#Se pintan las caras y se regresa una lista con los colores de las caras
Colores_puntos=detector_caras.Pintar_caras()
#Colores por cara

#Hacer el plano 2D de cubo
#print(Colores_puntos)
concatenacion.plano2D()

