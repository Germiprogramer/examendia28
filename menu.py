import ejercicio1.main as ej1
import ejercicio2.main as ej2
import ejercicio3.main as ej3
import ejercicio4.main as ej4
import ejercicio5.main as ej5

def iniciar():
    opcion = input("> ")

    if opcion == '1':
           ej1.main()

    if opcion == '2':
           ej2.main()

    elif opcion == '3':
            ej3.main()

    elif opcion == '4':
            ej4.main()

    elif opcion == '5':
            ej5.main()
    else:
        pass