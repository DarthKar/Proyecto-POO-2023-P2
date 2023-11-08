import pickle
class BaseDatos:
    def __init__(self):
        compradores = []
        vendedores = []
        productos = []
    
    def getCompradores(self):
        return self.compradores

    def getProductos(self):
        return self.productos
    
    def getVendedores(self):
        return self.vendedores

    def valoresPorDefecto(self):
        productos.append()