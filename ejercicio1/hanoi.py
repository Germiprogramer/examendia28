from pila import Pila, apilar, desapilar


pila1 = Pila()
pila2 = Pila()
pila3 = Pila()

def apilar_primera_torre(pila1, n):
    for i in range(n+1):
        apilar(pila1,i)


def torre_de_hanoi(n, pila1, pila2, pila3):
    if n==1:
        return 
    torre_de_hanoi(n-1, pila1, pila3, pila2)
    apilar(pila1,(desapilar(pila3)))
    torre_de_hanoi(n-1, pila3, pila2, pila1)

def hanoi_completo(n, pila1, pila2, pila3):
    apilar_primera_torre(pila1, n)
    torre_de_hanoi(n, pila1, pila2, pila3)

