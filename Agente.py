"""
Created on Tue Sep  8 14:29:59 2020

@author: PhoenixL

vector and matrix
V=[ 0 for j in range(3)]
from random import *
A=[[random() for i in range(Tcols)] for j in range(Trows)] 
#A of TrowsxTcols
len(A) rows
len(A[0]) columns


"""

import numpy as np
from random import *
from math import *
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as grafica


def normalizar(r,lb,ub):
    return (r-lb)/(ub-lb)

    

def desnormalizar(n,lb,ub):
    return n*(ub-lb)+lb


def maxp(V):
    #(val,pos)=maxp(V)
    n=len(V)
    pos=0
    val=V[pos]
    for e in range(n):
        if V[e]>val:
            val=V[e]
            pos=e          
            
    return val,pos

def minp(V):
    #(val,pos)=minp(V)
    n=len(V)
    pos=0
    val=V[pos]
    for e in range(n):
        if V[e]<val:
            val=V[e]
            pos=e    
    return val,pos

    
def DatabaseRead():
    #Database or table
    #DataBrute=DatabaseRead();
    #Excel reading
    #df = pd.read_excel('Desktop/Projects2020/PythonCurse/Neuralnetworks/datasetNN.xls')
    #df = pd.read_excel('datasample.xls')
    df = pd.read_excel('Base_Colores.xlsx',sheet_name="Base")
    Nrows=len(df); Ncols=len(df.columns)
    DataBrute = [[0 for i in range(Ncols)] for j in range(Nrows)]
    for r in range(Nrows):
        for c in range(Ncols):
            DataBrute[r][c]=df[df.columns[c]][r]
    return DataBrute
        


def plotgraph(V):
    N=len(V)
    D=[ j for j in range(N)]
    grafica.figure(1)
    grafica.plot(D,V,'b:',linewidth=2)
    grafica.xlabel('Número de datos')
    grafica.ylabel('Señal')
    grafica.show()

    #programa principal


def NormalData(DataExp):
###LMTT092018
###  (DataNorm,MRange)=NormalData(DataExp)
##
    Trows=len(DataExp)
    Tcols=len(DataExp[0])
    V = [0 for i in range(Trows)]
    MRange = [[0 for i in range(2)] for j in range(Tcols)] 
    DataNorm = [[0 for i in range(Tcols)] for j in range(Trows)] 
    for c in range(Tcols):
        for r in range(Trows):
            V[r]=DataExp[r][c]
        (valmax,posmax)=maxp(V)
        (valmin,posmin)=minp(V)    
        for r in range(Trows):
            DataNorm[r][c] = normalizar(DataExp[r][c],valmin,valmax)
        MRange[c][0]=valmin
        MRange[c][1]=valmax
    return DataNorm, MRange
    


def Hamming_Distance(V1,V2):
    B = len(V1)
    s=0
    for b in range(B):
        s = s + (V1[b]-V2[b])**2
    d = s**0.5
    k = 0
    for b in range(B):
        k = k + abs(V1[b]-V2[b]);
    m = (k+d)/2;
    return m 
    

def Agente(X,DB,MRange):
    Trows = len(DB)
    Tcols = len(DB[0])
    Xn = [ 0 for j in range(Tcols-1)];#Tcols-1 = total de entradas
    D = [ 0 for j in range(Trows)]
    V1 = [ 0 for j in range(Tcols-1)]
    V2 = [ 0 for j in range(Tcols-1)]
    y = 0
    for b in range(Tcols-1):
        Xn[b] = normalizar(X[b],MRange[b][0],MRange[b][1])
        
  
    for r in range(Trows):
        for c in range(Tcols-1):
            V1[c] = Xn[c]
            V2[c] = DB[r][c]
    
        #Cálculo de distancia Euclideana
        D[r] = Hamming_Distance(V1,V2)       
   
    #Distancia mínima
    (val,pos) = minp(D)
    
    #Extraer la respuesta
    y = DB[pos][Tcols-1]
    
    y = desnormalizar(y,MRange[Tcols-1][0],MRange[Tcols-1][1])
    
    return y
"""
(DataNorm,MRange)=NormalData(DatabaseRead())
X=[36,32,44]
r=Agente(X,DataNorm, MRange) 
print(r)  
""" 
    
    




