from src.base_datos.repositorio import Repositorio

class ProductoRepositorio:
    @staticmethod
    def guardar(producto) -> None:
        if producto is None:
            return
        Repositorio.guardar(producto)

    @staticmethod
    def get_producto_por_id(_id):
        return Repositorio.obtener_producto(_id)

    @staticmethod
    def get_productos():
        return Repositorio.obtener_productos()
