from typing import List, Optional
from src.base_datos.repositorio import Repositorio

class UsuarioRepositorio:
    @staticmethod
    def guardar(vendedor) -> None:
        if vendedor is None:
            return
        Repositorio.guardar_vendedor(vendedor)

    @staticmethod
    def obtener_por_id(_id: int):
        return Repositorio.obtener_vendedor_por_id(_id)

    @staticmethod
    def obtener():
        return Repositorio.obtener_vendedores()

    @staticmethod
    def eliminar(_id: int):
        Repositorio.eliminar_vendedor(_id)
