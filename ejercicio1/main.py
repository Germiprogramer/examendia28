from hanoi import pila1, pila2, pila3, hanoi_completo
from pila import imprimir

if __name__ == '__main__':
    hanoi_completo(5, pila1, pila2, pila3)
    print("Torre 1:")
    imprimir(pila1)
    print("Torre 2")
    imprimir(pila2)
    print("Torre 3")
    imprimir(pila3)