
from gestorAplicacion.entidad.Usuario.Usuario import Usuario
class Vendedor(Usuario):

    def __init__(self, id, nombre="jhon", apellido="doe", correo=None):
        if correo is None:
            correo = nombre + "@example.com" 
        super.__init__(id, nombre, apellido, correo)
        publicaciones = []
        opinionesVendedor = []
        compradores = []
        resenadores = []
    
    def getProductoVendedor(self):
        return self.publicaciones
    def agregarPublicacion(self,publicacion):
        if publicacion is not None:
            self.publicaciones.add(publicacion)

    def getOpinion(self):
        return self.opinionesVendedor
    def agregarOpinionVendedor(self, op):
        if op is not None:
            self.agregarOpinionVendedor.add(op)

    def existeResena(self, comprador):
        return self.resenadores.contains(comprador)
    
    def getCompradores(self):
        return self.compradores
    
    def getPublicaciones(self):
        return self.publicaciones
    
    def setPublicaciones(self, publicaciones):
        self.publicaciones = publicaciones
    
    def setOpinionesVendedor(self, opinionesVendedor):
        self.opinioneVendedor = opinionesVendedor
    
    def setCompradores(self, compradores):
        self.compradores = compradores

    def setResenadores(self, resenadores): 
        self.resenadores = resenadores
    def getResenadores(self):
        return self.resenadores
    
    def agregarComprador(self,comprador):
        self.compradores.add(comprador)
    
    def agregarResanador(self,resenador):
        self.resenadores.add(resenador)

    #Se necesita implementar mas metodos aqui. 

