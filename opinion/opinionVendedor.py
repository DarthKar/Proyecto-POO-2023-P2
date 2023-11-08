
from opinion import opinion
class opinionVendedor(opinion):

    def __init__(self, comentario, valoracion, comprador, vendedor):
        super.__init__(comentario, valoracion)
        self.comprador = comprador
        self.vendedor = vendedor

    def getComprador(self):
        return self.comprador
    def setComprador(self,comprador):
        self.comprador = comprador
    
    def getVendedor(self):
        return self.vendedor
    def setVendedor(self,vendedor):
        self.vendedor = vendedor
    
    def getComentario(self):
        return self.comentario
    def setComentario(self,comentario):
        self.comentario = comentario
    
    def getVendedor(self):
        return self.vendedor
