from typing import List, Optional
from gestor_aplicacion.entidad.producto.producto import Producto
from base_datos.repositorio import Repositorio

class ProductoRepositorio:
    @staticmethod
    def guardar(producto: Producto) -> None:
        if producto is None:
            return
        Repositorio.guardar(producto)

    @staticmethod
    def get_producto_por_id(_id: int) -> Optional[Producto]:
        return Repositorio.obtener_producto(_id)

    @staticmethod
    def get_productos() -> List[Producto]:
        return Repositorio.obtener_productos()
