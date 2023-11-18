class Publicacion(): #Debe implementar serializable

    def __init__(self, vendedor, producto, inventario, precio):
        self.vendedor = vendedor
        self.producto = producto
        self.inventario = inventario
        self.precio = precio
        self.oculto = False

        vendedor.agregarPublicacion(self)
        producto.agregarPublicacion(self)   

    def getVendedor(self):
        return self.vendedor
    
    def getProducto(self):
        return self.producto
    
    def getInventario(self):
        return self.inventario
    def setInventario(self, inventario):
        self.inventario = inventario

    def aumentarInventario(self, cantidad):
        if cantidad <=0:
            raise ValueError("La cantidad ingresada no es válida")
        self.inventario += cantidad

    def reducirInventario(self, cantidad):
        if cantidad <=0:
            raise ValueError("La cantidad ingresada no es válida")
        self.inventario-= cantidad

    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio
    
    def isOculto(self):
        return self.oculto
    def setOculto(self, oculto):
        self.oculto = oculto
    
    def mostrar_publicacion(self):
        return "\n------------------------------------------\n" + "Vendedor: " + self.vendedor.nombre + "\nProducto: " + self.producto.nombre + "\nInventario: " + str(self.inventario) + "\nPrecio: " + str(self.precio) + "\n------------------------------------------"