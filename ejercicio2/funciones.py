lista= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def sarrus_iterativo(lista):
    resultado = 0
    for i in range(3):
        resultado += lista[i%len(lista)][0]*lista[(i+1)%len(lista)][1]*lista[(i+2)%len(lista)][2]

    for i in range(3):
        resultado -= lista[0][i%len(lista)]*lista[1][(i+1)%len(lista)]*lista[2][(i+2)%len(lista)]
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
        print(escalar * determinante_recursivo(n-1, lista_nueva))
        return escalar * determinante_recursivo(n-1, lista_nueva)



print(determinante_recursivo(3, lista))








def sarrus_recursivo(lista00, lista11, lista22):
    pass


