import detector_caras
Colores_puntos=detector_caras.Pintar_caras()
concatenacion.plano2D()
#Valores dados de la lista
Centros=[]
problem=[]
for i in range(5,56,9):
    Centros.append(Colores_puntos[i])

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

print(solucion.split())

"""
    LBRL    U   RFBU    [:8]
    LFUU    R   BDDR    [9:17]
    RLBU    F   RLFB    [18:26]
    FLRR    D   BFDB    [27:35]
    DUDL    L   FUDD    [36:44]
    FRBU    B   DUFL    [45:53]
"""
cara_up=problema[:8]
cara_right=problema[9:17]
cara_front=problema[18:26]
cara_down=problema[27:35]
cara_left=problema[36:44]
cara_back=problema[45:53]
save_data_cara=[]
save_data_u=[]
save_data_r=[]
save_data_b=[]
save_data_l=[]
def Mov_Front():
    save_data_cara=cara_up.split()
    #Guardamos los datos de los latereales
    #Lateral_up
    save__data_u.append(save_data_cara[0])
    save__data_u.append(save_data_cara[1])
    save__data_u.append(save_data_cara[2])
    #Lateral right
    save__data_r.append(save_data_cara[2])
    save__data_r.append(save_data_cara[5])
    save__data_r.append(save_data_cara[8])
    #Lateral_bottom
    save__data_b.append(save_data_cara[8])
    save__data_b.append(save_data_cara[7])
    save__data_b.append(save_data_cara[6])
    #Lateral left
    save__data_l.append(save_data_cara[1])
    save__data_l.append(save_data_cara[3])
    save__data_l.append(save_data_cara[6])
    #Movemos
    save_data_cara[2]=save_data_u[0]
    save_data_cara[5]=save_data_u[1]
    save_data_cara[8]=save_data_u[2]

    save_data_cara[8]=save_data_r[0]
    save_data_cara[7]=save_data_r[1]
    save_data_cara[6]=save_data_r[2]

    save_data_cara[6]=save_data_b[0]
    save_data_cara[3]=save_data_b[1]
    save_data_cara[0]=save_data_b[2]

    save_data_cara[0]=save_data_l[0]
    save_data_cara[1]=save_data_l[1]
    save_data_cara[2]=save_data_l[2]
    #guardamos
    save__data.append(save_data_cara[8])
    save__data.append(save_data_cara[5])
    save__data.append(save_data_cara[8])

    save_data_cara[2]=save_data_cara[0]
    save_data_cara[5]=save_data_cara[1]
    save_data_cara[8]=save_data_cara[2]

"""    
def Mov_Afront():

def Mov_Up():

def Mov_Aup():

def Mov_Back():

def Mov_Aback():

def Mov_Right():

def Mov_Aright():

def Mov_Left():

def Mov_Aleft():

def Mov_Down():

def Mov_Adown():
"""