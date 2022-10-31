from funciones import listado_nombre, listado_longitud
from database import info_estrella, info_halcon

if __name__ == '__main__':
    entrada = int(input("Selecciona el numero del ejercicio: "))
    if entrada == 1:
            print("Las naves listadas por nombre:", listado_nombre("ejercicio3/starwars.csv"))
            print("Las naves listadas por longitud:" ,listado_longitud("ejercicio3/starwars.csv"))
    elif entrada == 2:
            print("Información Halcon Milenario: ", info_halcon)
            print("Información Estrella de la Muerte", info_estrella)
    elif entrada == 3:
    
    


