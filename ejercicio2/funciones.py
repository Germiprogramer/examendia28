lista= [
    [1,2,3],
    [4,5,6],
    [7,8,7]
]


def sarrus_iterativo(lista):
    resultado = 0
    for i in range(3):
        resultado += lista[i%len(lista)][0]*lista[(i+1)%len(lista)][1]*lista[(i+2)%len(lista)][2]

    for i in range(3):
        resultado -= lista[0][i%len(lista)]*lista[1][(i+1)%len(lista)]*lista[2][(i+2)%len(lista)]
    return resultado

def mult_positivos(lista00, lista11, lista22):
    i = 0
    while i <= 3:
        mult


def mult_negativos(matriz):
    pass


def sarrus_recursivo(lista00, lista11, lista22):
    


