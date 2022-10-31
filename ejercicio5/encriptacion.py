import hashlib

def encriptar(caracter):
    encriptado = hashlib.sha256(caracter.encode("utf-8")).hexdigest()
    ocho_carac = encriptado[0:8]
    return ocho_carac

def filtro_ascii(caracter):
    if ord(caracter) >= 32 and ord(caracter)<= 125:
        print("'{}' CARÁCTER VÁLIDO".format(caracter))
        return caracter
    else:
        print("'{}' CARÁCTER INVÁLIDO".format(caracter))
        return None

def encriptar_string(cadena):
    #seleccionamos los caracteres que debemos encriptar
    lista = []
    for i in range(len(cadena)):
        elemento = filtro_ascii(cadena[i])
        if elemento != None:
            lista.append(elemento)
    lista_encriptada = []
    for i in range(len(lista)):
        encriptado = encriptar(lista[i])
        lista_encriptada.append(encriptado)
    return lista_encriptada
    



        
    


