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
![image](https://user-images.githubusercontent.com/71536431/112432195-22e9cd00-8d06-11eb-9a06-2b08cf639978.png)

Para agregar más info tenemos que cambiar la linea del archivo "base_datos.py" para que los nuevos datos se anexen a la ultima fila de nuestra base de datos.
La hoja  de "base" es con la que trabaja el agente, para encontrar la mejor coicidencia entre los colores.

Codigo de reconocimiento de colores
Se buscaron los 5 colores más frecuentes de la imagen analizada, en este caso de cada punto.
![image](https://user-images.githubusercontent.com/71536431/112434645-701b6e00-8d09-11eb-974f-08101ba2f005.png)
y se va a desglozar en sus componentes BGR.


¿Cómo saber que detecta mi cámmara?
El formato que nos entrega el programa es BGR, por lo tanto decidimos crear una columna. Esta columna se pintara del color dpendiendo la combinacion del BGR que nos entregue.
![image](https://user-images.githubusercontent.com/71536431/112432756-f08c9f80-8d06-11eb-8b94-8e8166fbbe19.png)
El hecho de trabajar con una macro nos proporcionará algunos errores de compatibilidad- Por lo tanto, solo usaremos la macro para poner lo colores, pero no lo vamos a guardar como un archivo de macro.
Pasos:
Añadir una figura "xs"
Asiganrle una macro (Oprimir el boton de "nuevo")
![p1](https://user-images.githubusercontent.com/71536431/112432571-b58a6c00-8d06-11eb-8172-9d346d101790.png)
![p2](https://user-images.githubusercontent.com/71536431/112432836-0a2de700-8d07-11eb-8af9-81a1dbeadf6c.png)

Escribir el siguiente codigo en la macro
			lastrow = Cells(Rows.Count, 1).End(xlUp).Row
			For i = 2 To lastrow
			R = Range(Cells(i, 1), Cells(i, 1)).Value
			G = Range(Cells(i, 2), Cells(i, 2)).Value
			B = Range(Cells(i, 3), Cells(i, 3)).Value
			Range(Cells(i, 4), Cells(i, 4)).Interior.Color = RGB(B, G, R)
			Next i
		![Uploading image.png…]()


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

