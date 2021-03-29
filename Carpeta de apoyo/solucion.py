import kociemba
#kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
import configuracion
abre=configuracion.Abre_caras()

Colores_puntos=['', 'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Blanco', 'Rojo', 'Verde', 'Rojo', 'Amarillo', 'Verde', 'Verde', 'Naranja', 'Azul', 'Naranja', 'Naranja', 'Naranja', 'Blanco', 'Rojo', 'Azul', 'Azul', 'Amarillo', 'Blanco', 'Verde', 'Amarillo', 'Blanco', 'Blanco', 'Azul', 'Azul', 'Azul', 'Naranja', 'Rojo', 'Amarillo', 'Naranja', 'Verde', 'Amarillo', 'Blanco', 'Azul', 'Blanco', 'Blanco', 'Rojo', 'Rojo', 'Verde', 'Blanco', 'Amarillo', 'Rojo', 'Naranja', 'Azul', 'Rojo', 'Naranja', 'Azul', 'Amarillo', 'Verde', 'Verde', 'Amarillo']
print(len(Colores_puntos))
Centros=[]
problem=[]
for i in range(5,56,9):
    Centros.append(Colores_puntos[i])
print(Centros)

c=0
for punto in range(1,55):
    while Colores_puntos[punto]!=Centros[c]:
        c=c+1
    problem.append(abre[c])
    
    c=0
problema="".join(problem)
print(problema)
kociemba.solve(problema)