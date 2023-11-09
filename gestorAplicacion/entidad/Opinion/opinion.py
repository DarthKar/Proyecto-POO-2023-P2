
from opinionProducto import OpinionProducto
from opinionVendedor import OpinionVendedor
class opinion:
    
    def __init__(self, comentario, valoracion, creador=None):
        self.comentario = comentario
        self.valoracion= valoracion
        self.creador = creador

    def getComentario(self):
        return self.comentario
    def setComentario(self, op):
         self.comentario = op 
    
    def getValoracion(self):
        return self.valoracion
    def setValoracion(self, valoracion):
        self.valoracion = valoracion
    
    def getCreador(self):
        return self.creador
    def setCreador(self, creador):
        self.creador = creador


    def crearOpinionP(self, comprador, producto, comentario, valoracion):
        existe = False
        if (comprador in producto.getCompradores()):
            existe = True
            if (producto.existeResena(comprador)==False):
                opinion = OpinionProducto(comentario, valoracion, producto,comprador)
                opinion.setCreador(comprador)
                producto.addOpinionProducto(opinion)
                comprador.getResenasDeProductos().add(opinion)
                producto.agregarResenar(comprador)
                return "Se ha creado la resena con exito"
            return "Este usuario ya ha resenado el producto"
        if(existe==True):
            return "El usuario no ha comprado el producto, no se puede crear una resena"
        
        return "No se puede realizar la accion"
    
    def editarOpinionP(self, comprador, producto, comentario, valoracion):
        if(producto.existeResena(comprador)):
            for opinion in producto.getOpiniones():
                if (opinion.getCreador().equals(comprador)):

                    opinion.setComentario(comentario)
                    opinion.setValoracion(valoracion)
                    return "Se ha editado la resena con exito"
        return "Este comprador no tiene ninguna resena de este producto"

    def borrarOpinionP(self, producto, comprador):
        opinionEncontrada = False    
        opinionEliminar = None

        for opinionProducto in producto.getCompradores:
            if opinionProducto.getCreador().equals(comprador):
                opinionEncontrada = True
                opinionEliminar = opinionProducto
        if((opinionEncontrada and opinionProducto)!=None):
            return opinionEliminar
        return None


    def crearOpinionV(self, comprador, vendedor, comentario, valoracion):
        existe = False
        if (comprador in vendedor.getCompradores()):
            existe = True
            if (vendedor.existeResena(comprador)==False):
                opinion = OpinionVendedor(comentario, valoracion, vendedor,comprador)
                opinion.setCreador(comprador)
                vendedor.addOpinionProducto(opinion)
                comprador.getResenasDeVendedores().add(opinion)
                vendedor.agregarResenar(comprador)
                return "Se ha creado la resena con exito"
            return "Este usuario ya ha resenado el vendedor"
        if(existe==True):
            return "El usuario no es cliente de este vendedor, no se puede crear una resena"
        
        return "No se puede realizar la accion"
    
    def editarOpinionV(self, comprador, vendedor, comentario, valoracion):
        if(vendedor.existeResena(comprador)):
            for opinion in vendedor.getOpiniones():
                if (opinion.getCreador().equals(comprador)):

                    opinion.setComentario(comentario)
                    opinion.setValoracion(valoracion)
                    return "Se ha editado la resena con exito"
        return "Este comprador no tiene ninguna resena de este vendedor"

    def borrarOpinionV(self, vendedor, comprador):
        opinionEncontrada = False    
        opinionEliminar = None

        for opinionVendedor in vendedor.getCompradores:
            if opinionVendedor.getCreador().equals(comprador):
                opinionEncontrada = True
                opinionEliminar = opinionVendedor
        if((opinionEncontrada and opinionVendedor)!=None):
            return opinionEliminar
        return None


            
