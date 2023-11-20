
class BaseDatos:
    def __init__(self):
        self.compradores = []
        self.vendedores = []
        self.productos = []

    def get_compradores(self):
        return self.compradores

    def get_productos(self):
        return self.productos
    
    def get_vendedores(self):
        return self.vendedores
    
    def set_compradores(self, compradores):
        self.compradores = compradores
    
    def set_productos(self, productos):
        self.productos = productos

    def set_vendedores(self, vendedores):
        self.vendedores = vendedores