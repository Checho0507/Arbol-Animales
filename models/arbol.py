from .nodo import *
class Arbol:
    nodos = []
    respuestas = {}
    preguntas = {}

    def __init__(self):
        pass
    def agregarPreguntas(self,animal, pregunta, respuesta):
        self.respuestas[pregunta] = respuesta
        self.preguntas[animal] = pregunta

    def getNodos(self):
        return self.nodos

    def addNodo(self, nodo):
        self.nodos.append(nodo)


