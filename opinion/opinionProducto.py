
from opinion import opinion
class opinionProducto(opinion):

    def __init__(self,comentario, valoracion, producto, comprador):
        super.__init__(comentario,valoracion)
        self.comprador = comprador
        self.producto = producto

    def 