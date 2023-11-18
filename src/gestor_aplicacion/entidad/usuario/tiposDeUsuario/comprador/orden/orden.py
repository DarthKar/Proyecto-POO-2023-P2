from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.transaccion import Transaccion


class Orden(Transaccion):
    def __init__(self,id,comprador):
        super().__init__(id,comprador)
        pagar = False
        tieneDevoluciones = None

    def pagado(self):
        self.pagar = True
    
    def mostrar_producto_orden(orden):
        contador = 1
        for productos_transaccion in orden.get_productos_transaccion():
            print(f"{contador}. {productos_transaccion.mostrar_esp_producto()}")
            contador += 1

    def isTieneDevoluciones(self):
        return self.tieneDevoluciones
    
    def setTieneDevoluciones(self,tieneDevoluciones):
        self.tieneDevoluciones = tieneDevoluciones
    
    def mostrar_orden(self):
        return f"Comprado por: {self.comprador.get_nombre_completo()} \nID de la compra: {self.id}\nEl total a  pagar es: {self.calcular_total()}\n-------------------------------"

    def agregarProducto(self,productoTransaccion):
        self.productosTransaccion.append(productoTransaccion)
    
    def removerProducto(self,productoTransaccion):
        if productoTransaccion in self.productosTransaccion:
            self.productosTransaccion.remove(productoTransaccion)
    
    def modificarProducto(productoTransaccion,cantidad):
        productoTransaccion.setCantidad(cantidad)
    
    def isPagar(self):
        return self.pagar