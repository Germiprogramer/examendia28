
from funciones import crear_lista_de_listas, busqueda_binaria_recursiva, ordenacion_conteo, crear_dic

#ejercicio1
naves = crear_lista_de_listas("ejercicio3/starwars.csv")

print(naves)
#empleamos el algoritmo de busqueda para retornar el indice del elemento que buscamos
#indice_halcon = busqueda_binaria_recursiva("'HalcÃ³n Milenario")
#indice_estrella = busqueda_binaria_recursiva("Estrella de la Muerte")

#2
#creamos una nueva lista 
dic = crear_dic("ejercicio3/starwars.csv")
print(dic)


