from entidad.Usuario import Usuario
from orden import Carrito
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.Membresia import Membresia
from baseDatos.Impl.CompradorRepositorio import CompradorRepositorio

class Comprador(Usuario):
    def __init__(self, id, nombre, apellido, correo, membresia=Membresia.NINGUNA, saldo=100):
        super().__init__(id, nombre, apellido, correo)
        self._membresia = membresia
        self._saldo = saldo
        self._ordenes = []  
        self._devoluciones = []  
        self._resenasDeProductos = []
        self._productosComprados = []
        self._carrito = Carrito(id, self)

    def agregarProductoComprado(self,productoComprado):
        self._productosComprados.append(productoComprado)
    
    def getResenasDeProductos(self):
        return self._resenasDeProductos
    
    def getMembresia(self):
        return self._membresia
    
    def getOrdenes(self):
        return self._ordenes
    
    def agregarDevolucion(self, devolucion):
        if not devolucion.getProductosTransaccion():  
            self._saldo += self.AplicarDescuento(devolucion.calcularTotal())
            self._devoluciones.append(devolucion)
            CompradorRepositorio.guardar(self)
    
    def getCarrito(self):
        return self._carrito
    
    def getSaldo(self):
        return self._saldo

    def quitarSaldo(self,quitar):
        self._saldo = self._saldo - quitar
    
    #Segui agregando implementaciones....
    