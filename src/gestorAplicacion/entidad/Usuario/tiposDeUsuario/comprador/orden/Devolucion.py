from src.gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.Transaccion import Transaccion


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
    
    def modificar_producto(self,productotransaccion, cantidad):
        publicacion = productotransaccion.get_publicacion()

        if cantidad == productotransaccion.get_cantidad():
            return

        if cantidad == 0:
            self.removerProducto(productotransaccion)
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
    
    def getProductosDevolucion(self):
        productosDevolucion = []
        for productoOrden in self.orden.getProductosTransaccion():
            if not productoOrden.getPublicacion().getProducto().isPerecedero():
                coincide = False
                for productoDevolucion in self.productosTransaccion:
                    if productoOrden.getPublicacion() == productoDevolucion.getPublicacion():
                        coincide = True
                        break
                if not coincide:
                    productosDevolucion.append(productoOrden)
        return productosDevolucion

    def getOrdenProductoTransacction(self, publicacion):
        for productoOrden in self.orden.getProductosTransaccion():
            if productoOrden.getPublicacion() == publicacion:
                return productoOrden
        return None 
    



    
