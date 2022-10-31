from funciones import crear_lista_de_listas, crear_dic, seleccion, crear_dic,  ordenar_pasajeros, mostrar_info, nombres, listado_nombre, listado_longitud, nave_mas_tripu

#ejercicio1

#creamos un diccionario a partir del dataset
naves = crear_dic("ejercicio3/starwars.csv")

#creamos una lista con las naves

print(listado_nombre("ejercicio3/starwars.csv"))
print(listado_longitud("ejercicio3/starwars.csv"))
#_____________________________________________________________

info_estrella = mostrar_info("Estrella de la Muerte", naves, "nombre")
info_halcon = mostrar_info("Halcon Milenario", naves, "nombre")
#__________________________________________________________________-


print(ordenar_pasajeros("ejercicio3/starwars.csv"))

#____________________________________________________________

print(nave_mas_tripu("ejercicio3/starwars.csv"))

#_______________________________________--
#naves empiezan por AT
def primeras_letras(dataset):
    naves = crear_dic(dataset)
    nombres = []
    for i in range(len(naves)):
        nombres.append(naves[i]["nombre"])
    lista = []
    for i in range(len(nombres)):
        if [nombres[i]][0:2] == "At":
            lista.append(nombres[i])
    return lista

print(primeras_letras("ejercicio3/starwars.csv"))



#______________________________
#NAVES PUEDEN LLEVAR 6 O MAS PASAJEROS

def seisomas(data):
    naves = crear_dic(data)
    pasajeros = []
    for i in range(len(naves)):
        pasajeros.append(naves[i]["pasajeros"])

    filtrado = []
    for i in range(len(pasajeros)):
        
        if int(pasajeros[i]) > 6:
            filtrado.append(pasajeros[i])
    n = nombres(filtrado, "pasajeros", naves)
    return n

#print(seisomas("ejercicio3/starwars.csv"))


#______________________________
#INFORMACION NAVE MAS PEQUEÑA Y MAS GRANDE

def navepeque(data):
    naves = crear_dic(data)
    tamanio = []
    for i in range(len(naves)):
        tamanio.append(naves[i]["largo"])

    maspeque = tamanio[-1]
    for j in range(len(naves)):
        if naves[j]["largo"] == maspeque:
            respuesta = naves[j]["nombre"]
    return respuesta

def navegrande(data):
    naves = crear_dic(data)
    tamanio = []
    for i in range(len(naves)):
        tamanio.append(naves[i]["largo"])

    masgrande = tamanio[-1]
    for j in range(len(naves)):
        if naves[j]["largo"] == masgrande:
            respuesta = naves[j]["nombre"]
    return respuesta

print(navepeque("ejercicio3/starwars.csv"))






















