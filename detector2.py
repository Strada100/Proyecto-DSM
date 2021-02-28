from cv2 import cv2
import numpy as np
import configuracion
ncara=configuracion.nombre_caras()
#p1, p2, p3, p4, pc, p6, p7, p8, p9
def toma_fotos():
    k=0
    cap = cv2.VideoCapture(0)
    #El siguiente ciclo me permite tomar las fotos de las caras.
    #Al oprimir la tecla espacio se tomara la foto y en la terminal aparecerá el mensaje
    #La foto se guardara con el nombre de la cara

    while True:
        ret,frame = cap.read()
        if ret==True:
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

def recorta_fotos():
    k=0
    #El siguiente ciclo es para recortar las imagenes y que solo salga la cara del cubo
    #capitulo8
    for k in range(len(ncara)):
        image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[k]+'.jpg')
        print('image.shape=',image.shape)
        #image.shape= (480, 640, 3)
        imageOut=image[335:,260:435]
        cv2.imshow('Imagen de entrada',image)
        cv2.imshow('Imagen de salida',imageOut)
        img_name="Fotos_caras\Foto_cara_"+ncara[k]+'.jpg'
        cv2.imwrite(img_name, imageOut)
        print("Foto_cara_"+ncara[k]+' ha sido recortada')
        k=k+1
        #cv2.waitKey(0)
    cv2.destroyAllWindows()



def recortar_puntos():
    for p in range(0,6):
        image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[p]+'.jpg')
        ranx=image.shape[1]
        rany=image.shape[0]
        pre_scaler=5
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
                cv2.imwrite(Pname,Punto)
                #cv2.imshow('Punto '+str(k),Punto)
                k=k+1
            n=0
            l=l+1   
        #cv2.destroyAllWindows()

def fit_colors():
    cap = cv2.VideoCapture(0)
    #Mando a llamr del archivo configuracion los matices a detectar
    R2_rojo,R_azul,R_naranja,R_verde, R_amarillo=configuracion.matices()
    Blanco, Azul, Verde, Rojo, Amarillo, Naranja=configuracion.colores_basic()
    for n in range(1,6):
        image=cv2.imread('Fotos_caras\Foto_cara_'+ncara[n]+'.jpg') #leemos la imagen
        for k in range(1,9):
            
            frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            maskRed1 = cv2.inRange(frameHSV, R2_rojo[0], R2_rojo[1])
            maskRed2 = cv2.inRange(frameHSV, R2_rojo[2], R2_rojo[3])
            maskRed = cv2.add(maskRed1, maskRed2) #Como se puede ver en la imagen de HSV, el color rojo se parte
            maskBlue = cv2.inRange(frameHSV, R_azul[0], R_azul[1])
            maskOrange = cv2.inRange(frameHSV, R_naranja[0], R_naranja[1])
            maskGreen = cv2.inRange(frameHSV, R_verde[0], R_verde[1])
            maskYellow = cv2.inRange(frameHSV, R_amarillo[0], R_amarillo[1])
            #maskWhite=cv2.inRange(frameHSV, WhiteBajo, WhiteAlto)
            """
            #Las siguientes lineas no son necesarias, solo se usaron para ver si detectaba correctamente los colores.
            cv2.imshow('frame', image)
            cv2.imshow('Azul', maskBlue)
            cv2.imshow('Verde', maskGreen)
            cv2.imshow('Roja', maskRed)
            cv2.imshow('Amarilla', maskYellow)
            cv2.imshow('Naranja', maskOrange)
            #cv2.imshow('Blanca', maskWhite)
            """
    cv2.waitKey(0) 
    cap.release()
    cv2.destroyAllWindows()

recortar_puntos()