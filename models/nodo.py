class Nodo:
    nombre = ''
    listNodos = []
    def __init__(self, nombre):
        self.nombre = nombre
        self.listNodos.append(nombre)

    def getNodos(self):
        return self.listNodos
    def getNombre(self):
        return self.nombre