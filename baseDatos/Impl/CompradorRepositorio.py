import Repositorio
class CompradorRepositorio():   #Implementar Repositorio


    def guardarComprador(self,comprador):
        if comprador is not None:
            Repositorio.guardarC(comprador)
        return

    def obtenerPorId(id):
        return Repositorio.obtenerCompradorPorId(id)

    def obtenerCompradores():
        return Repositorio.obtenerCompradores()

    def eliminarComprador(id):
        Repositorio.eliminarComprador(id)   
