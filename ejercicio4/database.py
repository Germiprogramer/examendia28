#probamos las funciones principales de nuestro codigo

from polinomio import Polinomio, agregar_termino, restar, dividir, mostrar, eliminar, determinar

dosx = Polinomio()
xcuadrado = Polinomio()
agregar_termino(xcuadrado, 2, 1)
agregar_termino(dosx, 1, 2)

polresta = restar(dosx, xcuadrado)
print(mostrar(polresta))
nuevo_pol = dividir(xcuadrado, dosx)


agregar_termino(nuevo_pol, 1, 2)
agregar_termino(nuevo_pol, 2,1)
print(nuevo_pol.grado)
print(mostrar(nuevo_pol))
eliminar(nuevo_pol, 1)
print(mostrar(nuevo_pol))
print(determinar(nuevo_pol, 3))
