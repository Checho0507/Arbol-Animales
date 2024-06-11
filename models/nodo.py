class Nodo:
    def __init__(self, pregunta=None, animal=None):
        self._pregunta = pregunta
        self._animal = animal
        self._si = None
        self._no = None

    # Getters y setters para pregunta
    def get_pregunta(self):
        return self._pregunta

    def set_pregunta(self, pregunta):
        self._pregunta = pregunta

    # Getters y setters para animal
    def get_animal(self):
        return self._animal

    def set_animal(self, animal):
        self._animal = animal

    # Getters y setters para si
    def get_si(self):
        return self._si

    def set_si(self, si):
        self._si = si

    # Getters y setters para no
    def get_no(self):
        return self._no

    def set_no(self, no):
        self._no = no
