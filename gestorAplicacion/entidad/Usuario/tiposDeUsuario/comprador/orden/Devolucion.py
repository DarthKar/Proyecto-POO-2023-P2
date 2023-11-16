from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.Transaccion import Transaccion
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.Vendedor.Publicacion import Publicacion
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.ProductoTransaccion import ProductoTransaccion
class Devolucion(Transaccion):
    
    def __init__(self, id, comprador):
        super().__init__(id, comprador)
        self.orden = None

    def agregarProducto(self,productoTransaccion):
        publicacion = productoTransaccion.getPublicacion()
        publicacion.reducirInventario(productoTransaccion.getCantidad())
        self.productosTransaccion.append(productoTransaccion)
        self.orden.setTieneDevoluciones(True)
    
    def removerProducto(self,productoTransaccion):
        productoTransaccion.getPublicacion().aumentarInventario(productoTransaccion.getCantidad())
        self.productosTransaccion.remove(productoTransaccion)
        self.orden.setTieneDevoluciones(not not self.productosTransaccion)
    
    def modificar_producto(productotransaccion, cantidad):
        publicacion = productotransaccion.get_publicacion()

        if cantidad == productotransaccion.get_cantidad():
            return

        if cantidad == 0:
            removerProducto(productotransaccion)
            return

        if cantidad > productotransaccion.get_cantidad():
            diferencia = cantidad - productotransaccion.get_cantidad()
            publicacion.reducir_inventario(diferencia)
        else:
            diferencia = productotransaccion.get_cantidad() - cantidad
            publicacion.aumentar_inventario(diferencia)

        productotransaccion.set_cantidad(cantidad)

    def getOrden(self):
        return self.orden
    
    def setOrden(self, orden):
        self.orden = orden
    
    #Faltan dos metodos por favor implementarlos

    
