from encriptacion import encriptar_string
from hash import *

if __name__ == '__main__':
    cadena = str(input("Escribe la cadena a encriptar:  "))
    encriptaciones = encriptar_string(cadena)
    print(encriptaciones)


    tabla1 = Tabla_Hash(len(encriptaciones)*2)
    for i in range(len(encriptaciones)):
        tabla1.insertar(encriptaciones[i])

    print(tabla1.tabla)



