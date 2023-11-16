import os
import BaseDatos
import pickle
from gestorAplicacion.entidad.Usuario.tiposDeUsuario import Vendedor
from gestorAplicacion.entidad.Producto import producto
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador import Comprador


class Repositorio:
    baseDatos=None
    FILE = "basedatos.txt"
    PATH = os.path.join(os.getcwd(), "temp", "{}")
   
    
    @classmethod
    def leer(cls):
        if cls.crearDirectorio() or cls.crearArchivo():
            cls.baseDatos=BaseDatos()
            cls.guardarArchivo()
            return
    leer()
    @classmethod
    def guardarArchivo(cls):
        try:
             with open(cls.PATH,"wb") as archivo:
                  pickle.dump(cls.baseDatos,archivo)
        except Exception as e:
             raise RuntimeError(e)
    @classmethod
    def crearArchivo(cls):
        return not os.path.exists(os.path.join(cls.PATH.format(cls.FILE)))
    @classmethod
    def crearDirectorio(cls):
        try:
            path = os.path.join(cls.PATH.format(""))
            if os.path.exists(path):
                return False
            os.makedirs(path)
            return True
        except Exception as e:
            raise RuntimeError(e)
    @classmethod
    def guardarVendedor(cls, vendedor: Vendedor):
        pos = next((i for i, v in enumerate(cls.baseDatos.vendedores) if vendedor.id == v.id), None)

        if pos is None:
            cls.baseDatos.vendedores.append(vendedor)
        else:
            cls.baseDatos.vendedores[pos] = vendedor
        cls.guardarArchivo()

    @classmethod
    def guardarComprador(cls, comprador):
        pos = next((i for i, v in enumerate(cls.baseDatos.compradores) if comprador.id == v.id), None)

        if pos is None:
            cls.baseDatos.compradores.append(comprador)
        else:
            cls.baseDatos.compradores[pos] = comprador
        cls.guardarArchivo()

    @classmethod
    def guardarProducto(cls, producto):
        pos = next((i for i, v in enumerate(cls.baseDatos.productos) if producto.id == v.id), None)

        if pos is None:
            cls.baseDatos.productos.append(producto)
        else:
            cls.baseDatos.productos[pos] = producto
        cls.guardarArchivo()

    @classmethod
    def obtener_vendedor_por_id(cls, id):
        return next((v for v in cls.baseDatos.vendedores if v.id == id), None)

    @classmethod
    def obtener_vendedores(cls):
        return cls.baseDatos.vendedores

    @classmethod
    def eliminar_vendedor(cls, id):
        vendedor = cls.obtener_vendedor_por_id(id)
        if vendedor:
            cls.baseDatos.vendedores.remove(vendedor)
        else:
            raise ValueError("No existe el vendedor")

    @classmethod
    def obtenerCompradores(cls):
        return cls.baseDatos.compradores

    @classmethod
    def obtenerCompradorPorId(cls, id):
        return next((c for c in cls.baseDatos.compradores if c.id == id), None)

    @classmethod
    def obtener_producto(cls, id):
        return next((p for p in cls.baseDatos.productos if p.id == id), None)

    @classmethod
    def obtenerProductos(cls):
        return cls.baseDatos.productos
        

    @classmethod
    def eliminarComprador(cls, id):
        comprador = cls.obtener_comprador_por_id(id)
        if comprador:
            cls.baseDatos.compradores.remove(comprador)
        else:
            raise ValueError("No existe el comprador")
