import csv

def crear_dic(datos):
    with open(datos, "r") as f:
        reader = csv.DictReader(f, delimiter= ";")
        lista = list(reader)

    return lista

def crear_lista_de_listas(datos):

    with open(datos, "r") as f:
        reader =csv.reader(f)

        lista = []
        for i in reader:
            lista.append(i)
    return lista

def busqueda_binaria_recursiva(lista, izq, der, buscado):
 
    # Check base case
    if der >= izq:
 
        mid = (der + izq) // 2
 
        # If element is present at the middle itself
        if lista[mid] == buscado:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif int(lista[mid]) > int(buscado):
            return busqueda_binaria_recursiva(lista, izq, mid - 1, buscado)
             # Else the element can only be present in right subarray
        else:
            return busqueda_binaria_recursiva(lista, mid + 1, der, buscado)
 
    else:
        #si el elemento no esta presente
        return -1

def ordenacion_conteo(lista):
    maximo = max(lista)
    minimo = min(lista)

    lista_ordenada = [0] * len(lista)
    lista_conteo = [0] * (maximo +1 -minimo)

    #cuenta cuantas veces aparece un número en la lista
    for numero in lista:
        lista_conteo[numero -minimo] +=1
    print("Lista conteo:  ", lista_conteo)
    #suma cada posicion con sus predecesores, ahora nos dirá cuantos elementos menores o iguales que i existen en la col
    for i in range(1, len(lista_conteo)):
        lista_conteo[i] = lista_conteo[i] + lista_conteo[i-1]

    for i in reversed(range(0,len(lista))):
        lista_ordenada[lista_conteo[lista[i]- minimo]-1] = lista[i]
        lista_conteo[lista[i]-minimo]-= 1
    return lista_ordenada

