from entidad.Usuario import Usuario
from orden import Carrito
import Membresia

class Comprador(Usuario):
    def __init__(self,id,nombre,apellido,correo,membresia= Membresia.NINGUNA,saldo= 100):
        super().__init__(id,nombre,apellido,correo)
        self._membresia = membresia
        self._saldo = saldo
        _ordenes = []
        _devoluciones = []
        _resenasDeProductos = []
        _productosComprados = []
        _carrito = Carrito(id,self)

    def agregarProductoComprado(self,productoComprado):
        self._productosComprados.append(productoComprado)
    
    def getResenasDeProductos(self):
        return self._resenasDeProductos
    
    def getMembresia(self):
        return self._membresia
    
    def getOrdenes(self):
        return self._ordenes
    
    #Segui agregando implementaciones....
    