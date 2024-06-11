from models.nodo import Nodo

class ControlArbol:
    def __init__(self, arbol):
        self.arbol = arbol

    def aprender(self, nodo, animal_actual):
        print("Qué tipo de animal es?")
        nuevo_animal = input()
        print(f"Qué pregunta distinguiría a un {nuevo_animal} de un {animal_actual}?")
        nueva_pregunta = input()
        print(f"Si el animal fuera un {nuevo_animal}, cuál sería la respuesta? (si/no)")
        respuesta = input().lower()

        nuevo_nodo_animal = Nodo(animal=nuevo_animal)
        nodo.set_pregunta(nueva_pregunta)
        if respuesta == 'si':
            nodo.set_si(nuevo_nodo_animal)
            nodo.set_no(Nodo(animal=animal_actual))
        else:
            nodo.set_no(nuevo_nodo_animal)
            nodo.set_si(Nodo(animal=animal_actual))
        nodo.set_animal(None)

    def adivinar(self, nodo):
        if nodo.get_animal():
            print(f"Es un {nodo.get_animal()}?")
            respuesta = input().lower()
            if respuesta == 'si':
                print("Soy el más grande?")
            elif respuesta == 'no':
                self.aprender(nodo, nodo.get_animal())
        else:
            print(nodo.get_pregunta())
            respuesta = input().lower()
            if respuesta == 'si':
                if nodo.get_si():
                    self.adivinar(nodo.get_si())
                else:
                    self.aprender(nodo, "pájaro")  # asumiendo que el nodo original tenía "pájaro"
            elif respuesta == 'no':
                if nodo.get_no():
                    self.adivinar(nodo.get_no())
                else:
                    print("No sé qué es. Vamos a aprender!")
                    self.aprender(nodo, "pájaro")  # asumiendo que el nodo original tenía "pájaro"
