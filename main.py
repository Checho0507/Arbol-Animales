from models.arbol import Arbol
from controlers.controler import ControlArbol

def main():
    arbol = Arbol()
    control = ControlArbol(arbol)
    while True:
        print('Estás pensando en un animal? (si/no)')
        respuesta = input().lower()
        if respuesta == 'si':
            control.adivinar(arbol.get_raiz())
        elif respuesta == 'no':
            break

if __name__ == '__main__':
    main()
