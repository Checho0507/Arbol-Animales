from models.nodo import Nodo
from controlers.controlNodo import *
from models.absNodo import AbsNodo
from models.arbol import Arbol
def main():
    arbol = Arbol()
    nodoInicial = Nodo('pájaro')
    arbol.addNodo(nodoInicial)
    count = 0
    while (True):
        print('Estas pensando en un animal?')
        respuesta = input()
        if respuesta == 'Si':
            if count == 0:
                print(f'Es un {nodoInicial.getNombre()}?')
                respuesta = input()
                if respuesta == 'Si':
                    pass
                if respuesta == 'No':
                    print('Qué tipo de animal es?')
                    agregarNodo(arbol, nodoInicial)
                    count += 1
            else:
                animales = nodoInicial.getNodos()
                for i in range(len(animales)-1):
                    pregunta = arbol.preguntas[animales[i+1]]
                    print(f'{pregunta}')
                    respuesta = input()
                    respuesta2 = arbol.respuestas[pregunta]
                    validas = 0
                    if respuesta == respuesta2:
                        validas += 1
                    if validas == len(animales)-1:
                        print(f'Es un {animales[count]}?')
                        respuesta = input()
                        if respuesta == 'No':
                            print('Cómo se llama el animal?')
                            nodos = arbol.getNodos()
                            agregarNodo(arbol, nodos[i+1])
                        if respuesta == 'Si':
                            pass
        if respuesta == 'No':
            pass

if __name__ == '__main__':
    main()

