from tkinter import Frame

class FieldFrame(Frame):

    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__()
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado




    

    def getValue(self, criterio):
     
        pass
