import os
import pickle
from typing import List, Optional
from src.base_datos.base_datos import BaseDatos

class Repositorio:
    baseDatos = None
    FILE = "basedatos.pickle"
    PATH = os.path.join(os.getcwd(), "temp", "{}")

    @staticmethod
    def guardar(vendedor) -> None:
        pos = next((i for i, v in enumerate(Repositorio.baseDatos.getVendedores()) if vendedor.getId() == v.getId()), None)
        if pos is None:
            Repositorio.baseDatos.getVendedores().append(vendedor)
        else:
            Repositorio.baseDatos.getVendedores()[pos] = vendedor
        Repositorio.guardar_archivo()

    @staticmethod
    def guardar(comprador) -> None:
        pos = next((i for i, c in enumerate(Repositorio.baseDatos.getCompradores()) if comprador.getId() == c.getId()), None)
        if pos is None:
            Repositorio.baseDatos.getCompradores().append(comprador)
        else:
            Repositorio.baseDatos.getCompradores()[pos] = comprador
        Repositorio.guardar_archivo()

    @staticmethod
    def guardar(producto) -> None:
        pos = next((i for i, p in enumerate(Repositorio.baseDatos.getProductos()) if producto.getId() == p.getId()), None)
        if pos is None:
            Repositorio.baseDatos.getProductos().append(producto)
        else:
            Repositorio.baseDatos.getProductos()[pos] = producto
        Repositorio.guardar_archivo()

    @staticmethod
    def obtener_vendedor_por_id(_id: int):
        return next((v for v in Repositorio.baseDatos.getVendedores() if v.getId() == _id), None)

    @staticmethod
    def obtener_vendedores():
        return Repositorio.baseDatos.getVendedores()

    @staticmethod
    def eliminar_vendedor(_id: int) -> None:
        vendedor = Repositorio.obtener_vendedor_por_id(_id)
        if vendedor:
            Repositorio.baseDatos.getVendedores().remove(vendedor)
            Repositorio.guardar_archivo()

    @staticmethod
    def obtener_compradores():
        return Repositorio.baseDatos.getCompradores()

    @staticmethod
    def obtener_comprador_por_id(_id: int):
        return next((c for c in Repositorio.baseDatos.getCompradores() if c.getId() == _id), None)

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
            Repositorio.baseDatos.getCompradores().remove(comprador)
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
