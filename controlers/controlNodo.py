from models.nodo import Nodo
from models.arbol import Arbol
def agregarNodo(arbol, nodoInicial):
    respuesta = input()
    print(f'Qué tipo de pregunta distinguiría a un {respuesta} de un {nodoInicial.getNombre()}?')
    pregunta = input()
    print(f'Si el animal fuera un {respuesta} cuál sería la respuesta?')
    respuesta2 = input()
    arbol.agregarPreguntas(respuesta, pregunta, respuesta2)
    nodo = Nodo(respuesta)
    arbol.addNodo(nodo)
