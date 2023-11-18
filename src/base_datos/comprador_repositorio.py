from repositorio import Repositorio
class CompradorRepositorio():   #Implementar Repositorio


    def guardarComprador(self,comprador):
        if comprador is not None:
            Repositorio.guardar_comprador(comprador)
        return

    def obtenerPorId(id):
        return Repositorio.obtener_comprador_por_id(id)

    def obtenerCompradores():
        return Repositorio.obtener_compradores()

    def eliminarComprador(id):
        Repositorio.eliminar_comprador(id)
