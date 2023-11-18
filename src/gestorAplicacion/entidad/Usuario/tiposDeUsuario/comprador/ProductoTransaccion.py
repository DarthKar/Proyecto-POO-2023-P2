class ProductoTransaccion:
    def __init__(self,publicacion,cantidad):
        self.publicacion = publicacion
        self.cantidad = cantidad
    
    def getPublicacion(self):
        return self.publicacion
    
    def getCantidad(self):
        return self.cantidad
    
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    
    def getSubTotal(self):
        return self.getCantidad()*self.getPublicacion().getPrecio()
    
    def mostrarEspProducto(self):
        return "\n-----------------------------------------\n"+"Nombre: "+self.getPublicacion().getProducto().getNombre()+"\nCantidad: "+self.getCantidad()+"\nPrecio: "+self.getPublicacion().getPrecio()+"\nVendedor: "+self.getPublicacion().getVendedor().getNombre()+"\nSubtotal: "+self.getSubTotal()+"\n-----------------------------------------\n"
    