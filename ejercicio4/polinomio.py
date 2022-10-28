class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    #escalar de un polinomio

    def __init__(self,valor,termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1