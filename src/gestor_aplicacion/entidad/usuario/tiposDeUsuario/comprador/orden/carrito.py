from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.transaccion import Transaccion

class Carrito(Transaccion):
    def __init__(self,id,comprador):
        super().__init__(id,comprador)
    
    def mostrarCarrito(carrito):
        contador1 = 1
        for productosTransaccion in carrito.getProductosTransaccion():
            print(contador1 + ". " + productosTransaccion.mostrarEspProducto());
            contador1 += 1
        
    def agregar_producto(self,productoTransaccion):
        self.productosTransaccion.append(productoTransaccion)
    

    def remover_producto(self, productoTransaccion):
        if productoTransaccion in self.productosTransaccion:
            self.productosTransaccion.remove(productoTransaccion)
    
    
    def modificar_producto(self, productoTransaccion, cantidad):
        productoTransaccion.setCantidad(cantidad)                                                                       