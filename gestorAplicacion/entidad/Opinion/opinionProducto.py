
from opinion import opinion
class OpinionProducto(opinion):

    def __init__(self,comentario, valoracion, producto, comprador):
        super().__init__(comentario,valoracion)
        self.comprador = comprador
        self.producto = producto

    def getProducto(self):
        return self.producto
    def setProducto(self, producto):
        self.producto = producto
    
    def getComentario(self):
        return self.comentario
    def setComentario(self, comentario):
        self.comentario = comentario

    def getValoracion(self):
        return self.valoracion
    def setValoracion(self, valoracion):
        self.valoracion  = valoracion

    def getComprador(self):
        return self.comprador
    def setComprador(self, comprador):
        self.comprador = comprador
