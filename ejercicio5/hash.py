from operator import pos


def crear_tabla(tamanio):
    #Crea una tabla hash vacía
    tabla = [None]*tamanio
    return tabla

def cantidad_elementos_l(tabla):
    return (len(tabla) - tabla.count(None))

def bernstein(texto):
    h = 0
    for letra in texto:
        h = h*33 +ord(letra)
    return h

def funcion_hash(dato, tamanio_tabla):
    #hash por division en este caso
    return bernstein(dato)%tamanio_tabla

def agregar_l(tabla,dato):
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is None):
        tabla[posicion] = dato
    else:
        print("se produjo una colisión")

def buscar_l(tabla,buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if (tabla[posicion] is not None):
        if (buscado == tabla[posicion]):
            pos = posicion
        else:
            print("aplicar funcion de sondeo")

    return pos

def quitar_l(tabla, dato):
    dato = None 
    posicion = funcion_hash(dato, len(tabla))
    if tabla[posicion] is not None:
        if dato == tabla[posicion]:
            dato = tabla[posicion]
            tabla[posicion] = None
        else:
            print("aplicar funcion de sondeo")
            #aqui iria el codigo de la funcion de sondeo

    return dato

def cantidad_elementos_L(tabla):
    return sum(lista.tamanio for lista in tabla if lista is not None)