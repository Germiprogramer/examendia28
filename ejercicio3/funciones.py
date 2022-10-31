import csv

def crear_dic(datos):
    with open(datos, "r") as f:
        reader = csv.DictReader(f, delimiter= ";")
        lista = list(reader)

    return lista

def crear_lista_de_listas(datos):

    with open(datos, "r") as f:
        reader =csv.reader(f, delimiter= ";")

        lista = []
        for i in reader:
            lista.append(i)
            
        lista.pop(0)
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


def seleccion(lista):
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
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

def mostrar_info(nombre, dic, clave):
    
    
    indice = None
    for i in range(len(dic)):
        if dic[i][clave] == nombre:
            indice = i
    
    return dic[indice]

def nombres(lista, key, dic):
        "Metodo para obtener los nombres"
        lista2 = []
        for i in range(len(lista)):
            for j in range(len(dic)):
                if dic[j][key] == lista[i]:
                    lista2.append(dic[j]["nombre"]) 
        return lista2

def ordenar_pasajeros(naves):
    lista = crear_lista_de_listas(naves)
    lista_pasajeros = []
    for i in range(len(lista)):
        try:
            lista_pasajeros.append(lista[i][3])
        except:
            pass
    

    lista_ordenada = seleccion(lista_pasajeros)
    print(lista_ordenada)
    lista_naves_ordenadas = nombres(lista_ordenada, "pasajeros", crear_dic(naves))
    return lista_naves_ordenadas

def listado_nombre(data):
    naves = crear_dic(data)
    nombre_naves = []

    for i in range(len(naves)):
        nombre_naves.append(naves[i]["nombre"])
    
    naves_ordenadas = list(reversed(sorted(nombre_naves)))
    return naves_ordenadas

def listado_longitud(data):
    naves = crear_dic(data)
    longitud_naves = []
    for i in range(len(naves)):
        longitud_naves.append(naves[i]["largo"])

def nave_mas_tripu(dataset):
    naves = crear_dic(dataset)
    trip_naves = []
    for i in range(len(naves)):
        trip_naves.append(naves[i]["tripulacion"])
    orden = seleccion(trip_naves)
    elemento = orden[-1]
    for j in range(len(naves)):
        if naves[j]["tripulacion"] == elemento:
            respuesta = naves[j]["nombre"]
    return respuesta

    
    

