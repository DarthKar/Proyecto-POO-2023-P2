from src.base_datos.repositorio import Repositorio


class CompradorRepositorio:
    @staticmethod
    def guardar(comprador) -> None:
        if comprador is None:
            return
        Repositorio.guardar(comprador)

    @staticmethod
    def obtener_por_id(_id: int):
        return Repositorio.obtener_comprador_por_id(_id)

    @staticmethod
    def obtener():
        return Repositorio.obtener_compradores()

    @staticmethod
    def eliminar(_id: int) -> None:
        Repositorio.eliminar_comprador(_id)
