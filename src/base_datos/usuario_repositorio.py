from typing import List, Optional
from gestor_aplicacion.entidad.usuario.tiposDeUsuario.vendedor.vendedor import Vendedor
from base_datos.repositorio import Repositorio

class UsuarioRepositorio:
    @staticmethod
    def guardar(vendedor: Vendedor) -> None:
        if vendedor is None:
            return
        Repositorio.guardar(vendedor)

    @staticmethod
    def obtener_por_id(_id: int) -> Optional[Vendedor]:
        return Repositorio.obtener_vendedor_por_id(_id)

    @staticmethod
    def obtener() -> List[Vendedor]:
        return Repositorio.obtener_vendedores()

    @staticmethod
    def eliminar(_id: int) -> None:
        Repositorio.eliminar_vendedor(_id)
