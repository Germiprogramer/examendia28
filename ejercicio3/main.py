from funciones import listado_nombre, listado_longitud, ordenar_pasajeros, primeras_letras, navegrande, navepeque, seisomas
from database import info_estrella, info_halcon, nave_mas_tripu

if __name__ == '__main__':
    entrada = int(input("Selecciona el numero del ejercicio: "))
    datos = "ejercicio3/starwars.csv"
    if entrada == 1:
            print("Las naves listadas por nombre:", listado_nombre(datos))
            print("Las naves listadas por longitud:" ,listado_longitud(datos))
    elif entrada == 2:
            print("Información Halcon Milenario: ", info_halcon)
            print("Información Estrella de la Muerte", info_estrella)
    elif entrada == 3:
            print("Pasajeros ordenados: ", ordenar_pasajeros(datos))
    elif entrada ==4:
        print("Nave con mas tripulacion : ", nave_mas_tripu(datos))
    elif entrada ==5:
        print("Nave que empiezan por 'At' : ", primeras_letras(datos))
    elif entrada == 6:
        print("Naves con 6 o más tripulantes: ", seisomas(datos))
    elif entrada == 7:
        print("Nave más pequeña: ", navepeque(datos))
        print("Nave más grande: ", navegrande(datos))
    
    


