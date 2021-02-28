import cv2
import numpy as np
import configuracion
R2_rojo,R_azul,R_naranja,R_verde, R_amarillo, R_blanco=configuracion.matices()
 
image = cv2.imread('Fotos_caras\Foto_cara_left.jpg')
#cap = cv2.VideoCapture(0)
 
while(1):
    # Take each frame
    #_, frame = cap.read()
 
    # Convert BGR to HSV
    frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #definiendo los rangos, se van a usar los colores de los extremos
    #Cada color tendra dos mascaras.

    """
    # define range of blue color in HSV
    lower_verde = np.array([25,50,50])
    upper_verde = np.array([67,255,255])
    lower_rosa1 = np.array([125,50,50])
    upper_rosa1 = np.array([167,255,255])
 
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_verde, upper_verde)
    mask1 = cv2.inRange(hsv, lower_rosa1, upper_rosa1)
    """
    frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #Mascaras
    maskRed1 = cv2.inRange(frameHSV, R2_rojo[0], R2_rojo[1])
    #maskRed2 = cv2.inRange(frameHSV, R2_rojo[2], R2_rojo[3])
    maskRed = maskRed1#cv2.add(maskRed1, maskRed2) #Como se puede ver en la imagen de HSV, el color rojo se parte
    maskBlue = cv2.inRange(frameHSV, R_azul[0], R_azul[1])
    maskOrange = cv2.inRange(frameHSV, R_naranja[0], R_naranja[1])
    maskGreen = cv2.inRange(frameHSV, R_verde[0], R_verde[1])
    maskYellow = cv2.inRange(frameHSV, R_amarillo[0], R_amarillo[1])
    maskWhite = cv2.inRange(frameHSV, R_blanco[0], R_blanco[1])
    # Bitwise-AND mask and original image
    rojo = cv2.bitwise_and(image,image, mask= maskRed)
    naranja= cv2.bitwise_and(image,image, mask= maskOrange)
    amarillo = cv2.bitwise_and(image,image, mask= maskYellow)
    verde = cv2.bitwise_and(image,image, mask= maskGreen)
    azul = cv2.bitwise_and(image,image, mask= maskBlue)
    blanco = cv2.bitwise_and(image,image, mask= maskWhite)
    
    cv2.imshow('frame',image)
    cv2.imshow('Azul',azul)
    cv2.imshow('Rojo',rojo)
    cv2.imshow('Naranja',naranja)
    cv2.imshow('Amarillo',amarillo)
    cv2.imshow('Verde',verde)
    cv2.imshow('Blanco',blanco)
    
 
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
 
cv2.destroyAllWindows()