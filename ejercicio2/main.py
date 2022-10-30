
from funciones import sarrus_iterativo, determinante_recursivo
import doctest

if __name__ == '__main__':
    #matriz ejemplo
    lista= [
        [1,2,3],
        [4,5,6],
        [9,8,9]
    ]

    print(sarrus_iterativo(lista))
    print(determinante_recursivo(3, lista))

    #mirar como se hacen los test
    doctest.testmod()
    
    
    

