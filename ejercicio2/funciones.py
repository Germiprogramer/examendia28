import doctest

def sarrus_iterativo(lista):
    resultado = 0
    for i in range(3):
        resultado += lista[(i-1)%len(lista)][0]*lista[(i)%len(lista)][1]*lista[(i+1)%len(lista)][2]

    for i in range(3):
        resultado -= lista[0][(i-1)%len(lista)]*lista[1][(i+1)%len(lista)]*lista[2][(i)%len(lista)]
    return resultado

def determinante_recursivo(n, lista):
    if n == 1:
        return n
    for i in range(n-1):
        escalar= lista[0][i]
        lista_nueva = []
        for j in range(n-1):
            lista_nueva.append(lista[j+1])
            
            lista_nueva[j].pop(i)
        
        return escalar * determinante_recursivo(n-1, lista_nueva)












