import hashlib


    #retornará un lista de caracteres troceada, que nos sera util para luego aplicar las tablas hash


lista = []
encriptado = hashlib.sha256(b"hola").hexdigest()
longitud = len(encriptado)

print(encriptado)
    
    #tocho
hashlib.sha256(b"El Libro de Python").hexdigest()
print(hashlib.sha224(b"El Libro de Python").hexdigest())
print(hashlib.sha512(b"El Libro de Python").hexdigest())
print(hashlib.blake2b(b"El Libro de Python").hexdigest())
print(hashlib.blake2s(b"El Libro de Python").hexdigest())
print(hashlib.blake2s(b"El Libro de Python").hexdigest())
print(hashlib.md5(b"El Libro de Python").hexdigest())

print(lista)


