
class CompradorRepositorio():   #Implementar Repositorio


    def guardar(self,comprador):
        if comprador is not None:
            Repositorio.guardar(comprador)
        return

    def obtenerPorId(id):
        return Repositorio.obtenerCompradorPorId(id)

    def obtener():
        return Repositorio.obtenerCompradores()

    def eliminar(id):
        Repositorio.eliminarComprador(id)   
