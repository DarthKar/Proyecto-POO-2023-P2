import os
import pickle
from typing import List, Optional
from src.base_datos.base_datos import BaseDatos

class Repositorio:
    baseDatos = None
    FILE = "basedatos.pickle"
    PATH = os.path.join(os.getcwd(), "temp", "{}")

    @staticmethod
    def guardar_vendedor(vendedor) -> None:
        pos = next((i for i, v in enumerate(Repositorio.baseDatos.get_vendedores()) if vendedor.getId() == v.getId()), None)
        if pos is None:
            Repositorio.baseDatos.get_vendedores().append(vendedor)
        else:
            Repositorio.baseDatos.get_vendedores()[pos] = vendedor
        Repositorio.guardar_archivo()

    @staticmethod
    def guardar_comprador(comprador) -> None:
        pos = next((i for i, c in enumerate(Repositorio.baseDatos.get_compradores()) if comprador.getId() == c.getId()), None)
        if pos is None:
            Repositorio.baseDatos.get_compradores().append(comprador)
        else:
            Repositorio.baseDatos.get_compradores()[pos] = comprador
        Repositorio.guardar_archivo()

    @staticmethod
    def guardar_producto(producto) -> None:
        pos = next((i for i, p in enumerate(Repositorio.baseDatos.getProductos()) if producto.getId() == p.getId()), None)
        if pos is None:
            Repositorio.baseDatos.getProductos().append(producto)
        else:
            Repositorio.baseDatos.getProductos()[pos] = producto
        Repositorio.guardar_archivo()

    @staticmethod
    def obtener_vendedor_por_id(_id: int):
        return next((v for v in Repositorio.baseDatos.get_vendedores() if v.getId() == _id), None)

    @staticmethod
    def obtener_vendedores():
        return Repositorio.baseDatos.get_vendedores()

    @staticmethod
    def eliminar_vendedor(_id: int) -> None:
        vendedor = Repositorio.obtener_vendedor_por_id(_id)
        if vendedor:
            Repositorio.baseDatos.get_vendedores().remove(vendedor)
            Repositorio.guardar_archivo()

    @staticmethod
    def obtener_compradores():
        return Repositorio.baseDatos.get_compradores()

    @staticmethod
    def obtener_comprador_por_id(_id: int):
        return next((c for c in Repositorio.baseDatos.get_compradores() if c.getId() == _id), None)

    @staticmethod
    def obtener_producto(_id: int):
        return next((p for p in Repositorio.baseDatos.getProductos() if p.getId() == _id), None)

    @staticmethod
    def obtener_productos():
        return Repositorio.baseDatos.get_productos()

    @staticmethod
    def eliminar_comprador(_id: int) -> None:
        comprador = Repositorio.obtener_comprador_por_id(_id)
        if comprador:
            Repositorio.baseDatos.get_compradores().remove(comprador)
            Repositorio.guardar_archivo()

    @staticmethod
    def guardar_archivo() -> None:
        with open(Repositorio.PATH.format(Repositorio.FILE), 'wb') as file:
            pickle.dump(Repositorio.baseDatos, file)

    @staticmethod
    def leer(base_datos):
        if Repositorio.crear_directorio() or Repositorio.crear_archivo() or base_datos is not None:
            Repositorio.baseDatos = base_datos
            Repositorio.guardar_archivo()
            return False

        try:
            with open(Repositorio.PATH.format(Repositorio.FILE), 'rb') as file:
                Repositorio.baseDatos = pickle.load(file)
                return True
        except (IOError, EOFError, pickle.PickleError, AttributeError, ModuleNotFoundError) as e:
            raise RuntimeError(e)

    @staticmethod
    def crear_archivo() -> bool:
        return not os.path.exists(Repositorio.PATH.format(Repositorio.FILE))

    @staticmethod
    def crear_directorio() -> bool:
        try:
            path = Repositorio.PATH.format("")
            if os.path.exists(path):
                return False
            os.makedirs(path)
            return True
        except OSError as e:
            raise RuntimeError(e)
