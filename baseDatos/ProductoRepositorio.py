from baseDatos.Impl import Repositorio
class ProductoRepositorio():


    def guardarProducto(self,producto):
        if producto is not None:
            Repositorio.guardarP(producto)
        return
    
    def getProductoPorId(id):
        return Repositorio.getProducto(id)
    
    def obtenerProductos():
        return Repositorio.obtenerProductos()