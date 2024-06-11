class AbsNodo:
    pregunta = ''
    def __init__(self, pregunta):
        self.pregunta = pregunta
    def getPregunta(self):
        return self.pregunta
    def setPregunta(self, new):
        self.pregunta = new
