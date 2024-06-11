from models.nodo import Nodo

class Arbol:
    def __init__(self):
        self._raiz = Nodo(pregunta="Es un pájaro?", animal=None)
        self._raiz.set_si(Nodo(animal="pájaro"))

    def get_raiz(self):
        return self._raiz
