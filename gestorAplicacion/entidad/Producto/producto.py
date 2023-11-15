import categoria
from baseDatos.Impl import ProductoRepositorio
class Producto:
    def __init__(self,id,nombre,categoria):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        _opinion = []
        _compradores = []
        _publicaciones = []
        _resenadores = []

        def addopinionProducto(resena):
            if resena is not None:
                _opinion.append(resena)
        
        def existeResena(comprador):
            return comprador in self._resenadores
        
        def getId(self):
            return self.id
        
        def getNombre(self):
            return self.nombre
        
        def getCategoria(self):
            return self.categoria
        
        def getopiniones(self):
            return self._opinion
        
        def getPublicaciones(self):
            return self._publicaciones
        
        def agregarPublicacion(self,publicacion):
            _publicaciones.append(publicacion)
        
        def setId(self,id):
            self.id = id
        
        def setNombre(self,nombre):
            self.nombre = nombre
        
        def setCategoria(self,categoria):
            self.categoria = categoria
        
        def setcompradores(self,compradores):
            self._compradores = compradores
        
        def get_compradores(self):
            return self._compradores
        
        def getresenadores(self):
            return self._resenadores

        def setopinion(self,opinion):
            self._opinion = opinion
        
        def setcompradores(self,compradores):
            self._compradores = compradores
        
        def setresenadores(self,resenadores):
            self._resenadores = resenadores
        
        def is_perecedero(self):
            return self.categoria.perecedero

        def agregarComprador(self,comprador):
            _compradores.append(comprador)
        
        def agregarResenador(self,resenador):
            _resenadores.append(resenador)

        def getProductos():
            return ProductoRepositorio.getProducto()
        #Seguir copiando el codigo....
