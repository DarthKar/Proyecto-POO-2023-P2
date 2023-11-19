from typing import List, Optional
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.comprador import Comprador
from src.base_datos.repositorio import Repositorio

class CompradorRepositorio:
    @staticmethod
    def guardar(comprador: Comprador) -> None:
        if comprador is None:
            return
        Repositorio.guardar(comprador)

    @staticmethod
    def obtener_por_id(_id: int) -> Optional[Comprador]:
        return Repositorio.obtener_comprador_por_id(_id)

    @staticmethod
    def obtener() -> List[Comprador]:
        return Repositorio.obtener_compradores()

    @staticmethod
    def eliminar(_id: int) -> None:
        Repositorio.eliminar_comprador(_id)

