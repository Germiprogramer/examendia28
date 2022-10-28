import hashlib

def encriptacion(mensaje):
    #retornará un lista de caracteres troceada, que nos sera util para luego aplicar las tablas hash
    
    lista = []
    encriptado = hashlib.sha256([b] mensaje).hexdigest()
    longitud = len(encriptado)
    
    #tocho
    lista.append(mensaje[0:longitud//8])
    lista.append(mensaje[(longitud//8):(longitud//8)*2])
    lista.append(mensaje[(longitud//8)*2:(longitud//8)*3])
    lista.append(mensaje[(longitud//8)*3:(longitud//8)*4])
    lista.append(mensaje[(longitud//8)*4:(longitud//8)*5])
    lista.append(mensaje[(longitud//8)*5:(longitud//8)*6])
    lista.append(mensaje[(longitud//8)*6:(longitud//8)*7])
    lista.append(mensaje[(longitud//8)*7:longitud])

    return lista

