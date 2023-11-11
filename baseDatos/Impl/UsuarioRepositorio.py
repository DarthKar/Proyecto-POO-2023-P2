
class VendedorRepositorio():


    def guardarVendedor(self,producto):
        if producto is not None:
            Repositorio.guardarU(producto)
        return
     
    def obtenerPorId(id):
        return Repositorio.obtenerVendedorPorId()

    def obtenerVendedores():
        return Repositorio.obtenerVendedores()
    
    def eliminarVendedor():
        Repositorio.eliminarVendedor()