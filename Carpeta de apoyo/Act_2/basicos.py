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
    return (r-lb)/(ub-lb);

    

def desnormalizar(n,lb,ub):
    return n*(ub-lb)+lb;


def maxp(V):
    #(val,pos)=maxp(V)
    n=len(V);
    pos=0;
    val=V[pos];
    for e in range(n):
        if V[e]>val:
            val=V[e];
            pos=e;          
            
    return val,pos

def minp(V):
    #(val,pos)=minp(V)
    n=len(V);
    pos=0;
    val=V[pos];
    for e in range(n):
        if V[e]<val:
            val=V[e];
            pos=e;
            
    return val,pos

    
def DatabaseRead():
    #Database or table
    #DataBrute=DatabaseRead();
    #Excel reading
    #df = pd.read_excel('Desktop/Projects2020/PythonCurse/Neuralnetworks/datasetNN.xls')
    df = pd.read_excel('datasample.xls')
    Nrows=len(df); Ncols=len(df.columns);
    DataBrute = [[0 for i in range(Ncols)] for j in range(Nrows)]; 
    for r in range(Nrows):
        for c in range(Ncols):
            DataBrute[r][c]=df[df.columns[c]][r];
    return DataBrute
        


def plotgraph(V):
    N=len(V);
    D=[ j for j in range(N)]
    grafica.figure(1)
    grafica.plot(D,V,'b:',linewidth=2)
    grafica.xlabel('Número de datos')
    grafica.ylabel('Señal')
    grafica.show()

    #programa principal



