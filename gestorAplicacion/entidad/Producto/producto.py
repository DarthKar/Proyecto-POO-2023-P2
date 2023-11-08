import categoria
class Producto:
    def __init__(self,id,nombre,categoria):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        opinion = []
        compradores = []
        publicaciones = []
        resenadores = []

        def addOpinionProducto(resena):
            if resena is not None:
                opinion.append(resena)
        
        def existeResena(comprador):
            return comprador in self.resenadores
        
        def getId(self):
            return self.id
        
        def getNombre(self):
            return self.nombre
        
        def getCategoria(self):
            return self.categoria
        
        def getOpiniones(self):
            return self.opinion
        
        def getPublicaciones(self):
            return self.publicaciones
        
        def agregarPublicacion(self,publicacion):
            publicaciones.append(publicacion)
        
        def setId(self,id):
            self.id = id
        
        def setNombre(self,nombre):
            self.nombre = nombre
        
        def setCategoria(self,categoria):
            self.categoria = categoria
        
        def setCompradores(self,compradores):
            self.compradores = compradores
        
        def getCompradores(self):
            return self.compradores
        
        def getResenadores(self):
            return self.resenadores

        def setOpinion(self,opinion):
            self.opinion = opinion
        
        def setCompradores(self,compradores):
            self.compradores = compradores
        
        def setResenadores(self,resenadores):
            self.resenadores = resenadores
        
        def is_perecedero(self):
            return self.categoria.perecedero

        def agregarComprador(self,comprador):
            compradores.append(comprador)
        
        def agregarResenador(self,resenador):
            resenadores.append(resenador)

        #Seguir copiando el codigo....
