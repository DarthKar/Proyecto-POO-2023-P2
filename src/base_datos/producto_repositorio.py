import repositorio
class ProductoRepositorio():

    def guardarProducto(self,producto):
        if producto is not None:
            Repositorio.guardarP(producto)
        return
    
    def getProductoPorId(id):
        return Repositorio.getProducto(id)
    
    def obtenerProducto():
        return Repositorio.Repositorio.obtener_productos()