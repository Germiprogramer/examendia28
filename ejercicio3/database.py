from funciones import navepeque, navegrande, seisomas, crear_dic, primeras_letras, crear_dic,  ordenar_pasajeros, mostrar_info, nombres, listado_nombre, listado_longitud, nave_mas_tripu

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


print(primeras_letras("ejercicio3/starwars.csv"))



#______________________________
#NAVES PUEDEN LLEVAR 6 O MAS PASAJEROS

#print(seisomas("ejercicio3/starwars.csv"))

#______________________________
#INFORMACION NAVE MAS PEQUEÑA Y MAS GRANDE


print(navepeque("ejercicio3/starwars.csv"))






















