from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.itransaccion import ITransaccion


class Transaccion(ITransaccion):
    def __init__(self,id,comprador):
        self.id = id
        self.comprador = comprador
        self.productosTransaccion = []
    
    def getComprador(self):
        return self.comprador
    
    def getProductosTransaccion(self):
        return self.productosTransaccion
    
    def setProductosTransaccion(self,productoTra):
        self.getProductosTransaccion = productoTra

    def getId(self):
        return self.id
    
    def calcular_total(productos_transaccion):
        total = 0
        for pro_tran in productos_transaccion:
            total += pro_tran.get_subtotal()
        return total
    
