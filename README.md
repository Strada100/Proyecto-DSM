# DSM
Este proyecto es para realizar una maquina capaz de solucionar el cubo rubik de 3x3. Se usará OpenCV.
1era tarea:
Identificacion de caras del cubo rubik. 
La idea de la identificacion de las caras viene de este video: https://youtu.be/_sL6TBVg-NU

Carpetas
"Caras digitalizadas" contiene las caras que fabricamos para ponerla en el plano 2D
"Fotos caras" contiene las 6 caras tomadas con la camara de la laptop y dentro de esta esta otras carpetas donde se recortaron cada punto de las caras para sy procesamiento.
"carpeta de apoyo" no es relevante, fueron archivos que sirvieron de apoyo para hacer pruebas.

"Base_Colores.xlsx" es nuestra base de datos. 
En la hoja de "recepcion" se puede visualizar lo que mandamos a la base si es que queremos añadir más informacion.
Para agregar más info tenemos que cambiar la linea del archivo "base_datos.py" para que los nuevos datos se anexen a la ultima fila de nuestra base de datos.
La hoja  de "base" es con la que trabaja el agente, para encontrar la mejor coicidencia entre los colores.


Archivos
Se realizó una base de datos donde se guardo los valores BGR obtenidos con el analisis de la imagen en el archivo "base de datos.py"
Archivos del programa
"main.py" el archivo donde se ejecutara todo el programa de reconocimiento de caras y la visualizacion de las caras digitales.
"detector.py" corresponde al archivo que nos permite tomar fotos, recortarlas y recortar los 9 puntos de la cara.
Tambien nos permite crear las caras digitales, asi como modificarlas.
"concatenacion.py" nos permite visualizar el cubo en 2D.
"configuracion.py" alamacena todas las configuraciones de nuestro programa.
"base_datos.py" nos permite leer el valor de la imagen en formato BGR y alamcenarlo en una base de datos.
"Agente.py" es el codigo correspondiente a la aprte de analisi para predecir el color que se esta visualizado a partir de los datos almacenados en la base de datos.

![ejemplo1](https://user-images.githubusercontent.com/71536431/112431264-e4074780-8d04-11eb-895f-e3288a8acd7d.jpeg)
 En la imagen anterior se puede visualizar el resultado del reconocimiento. Solo se necesita tomar en el orden correcto y en su orientacion correcta.
# Proyecto-DSM

