from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.transaccion import Transaccion


class Orden(Transaccion):
    def __init__(self,id,comprador):
        super().__init__(id,comprador)
        self.pagar = False
        self.tiene_devoluciones = False

    def pagado(self):
        self.pagar = True
    
    def mostrar_producto_orden(orden):
        contador = 1
        for productos_transaccion in orden.get_productos_transaccion():
            print(f"{contador}. {productos_transaccion.mostrar_esp_producto()}")
            contador += 1

    def isTieneDevoluciones(self):
        return self.tiene_devoluciones
    
    def setTieneDevoluciones(self,tieneDevoluciones):
        self.tiene_devoluciones = tieneDevoluciones
    
    def mostrar_orden(self):
        return f"Comprado por: {self.comprador.get_nombre_completo()} \nID de la compra: {self.id}\nEl total a  pagar es: {self.calcular_total()}\n-------------------------------"

    def agregar_producto(self, productoTransaccion):
        self.productosTransaccion.append(productoTransaccion)
    
    def remover_producto(self, productoTransaccion):
        if productoTransaccion in self.productosTransaccion:
            self.productosTransaccion.remove(productoTransaccion)
    
    def modificar_producto(self, productoTransaccion, cantidad):
        productoTransaccion.setCantidad(cantidad)
    
    def isPagar(self):
        return self.pagar
