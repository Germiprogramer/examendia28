from pila import Pila, apilar, imprimir, condicion_hanoi


pila4 = Pila()
pila5 = Pila()
pila6 = Pila()

apilar(pila5, 10)
apilar(pila6,10)

for i in range(4+1):
    apilar(pila4,i)
imprimir(pila4)

def hanoi(pila1, pila2, pila3):
    while True:
        try:
            condicion_hanoi(pila1,pila2)
        except:
            try:
                condicion_hanoi(pila1, pila3)
            except:
                try:
                    condicion_hanoi(pila2, pila3)
                except:
                    try:
                        condicion_hanoi(pila1, pila2)
                        imprimir(pila1)
                    except:
                        try:
                            condicion_hanoi(pila3, pila1)
                        except:
                            break
    return imprimir(pila1), imprimir(pila2), imprimir(pila3)

hanoi(pila4, pila5, pila6)