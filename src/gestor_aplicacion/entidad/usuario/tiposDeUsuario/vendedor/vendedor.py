from src.gestor_aplicacion.entidad.usuario.usuario import Usuario
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.vendedor.publicacion import Publicacion
from collections import defaultdict
from src.base_datos.comprador_repositorio import CompradorRepositorio


class Vendedor(Usuario):

    def __init__(self, id, nombre="jhon", apellido="doe", correo=None):
        super().__init__(id, nombre, apellido, correo)
        self.publicaciones = []
        self.opinionesVendedor = []
        self.compradores = []
        self.resenadores = []
    
    def getProductoVendedor(self):
        return self.publicaciones
    def agregarPublicacion(self,publicacion):
        if publicacion is not None:
            self.publicaciones.append(publicacion)

    def getOpinion(self):
        return self.opinionesVendedor
    def agregarOpinionVendedor(self, op):
        if op is not None:
            self.opinionesVendedor.append(op)

    def existeResena(self, comprador):
        return comprador in self.resenadores
    
    def getCompradores(self):
        return self.compradores
    
    def getPublicaciones(self):
        return self.publicaciones
    
    def setPublicaciones(self, publicaciones):
        self.publicaciones = publicaciones
    
    def setOpinionesVendedor(self, opinionesVendedor):
        self.opinioneVendedor = opinionesVendedor
    
    def setCompradores(self, compradores):
        self.compradores = compradores

    def setResenadores(self, resenadores): 
        self.resenadores = resenadores
    def getResenadores(self):
        return self.resenadores
    
    def agregarComprador(self,comprador):
        self.compradores.append(comprador)
    
    def agregarResenador(self,resenador):
        self.resenadores.append(resenador)

    @staticmethod
    def mejorVendendor():
        cantidadProductosPorVendedor = defaultdict(int)

        for comprador in CompradorRepositorio.obtener():
            for transaccion in comprador.getOrdenes():
                for productotransaccion in transaccion.getProductosTransaccion():
                    vendedor = productotransaccion.getPublicacion().getVendedor()
                    cantidadProductosPorVendedor [vendedor] += 1

        mejorVendedor = None
        maxCantidadProductos = 0

        for vendedor, cantidadProductos in cantidadProductosPorVendedor.items():
            if cantidadProductos > maxCantidadProductos:
                maxCantidadProductos = cantidadProductos
                mejorVendedor = vendedor

        if mejorVendedor:
            return f"{mejorVendedor.nombre} {mejorVendedor.apellido} con un total de {maxCantidadProductos} productos vendidos"
        else:
            return "No se encontró mejor vendedor"

    @staticmethod
    def mejorVendedorPorRecaudacion():
    
        recaudacionPorVendedor = {}

        for comprador in CompradorRepositorio.obtener():
            for orden in comprador.getOrdenes():
                for productoTransaccion in orden.getProductosTransaccion():
                    vendedor = productoTransaccion.getPublicacion().getVendedor()
                    precioProducto = productoTransaccion.getPublicacion().getPrecio()

                    if vendedor in recaudacionPorVendedor:
                        recaudacionPorVendedor[vendedor] += precioProducto
                    else:
                        recaudacionPorVendedor[vendedor] = precioProducto

        mejorVendedor = None
        maxRecaudacion = 0

        for vendedor, recaudacion in recaudacionPorVendedor.items():
            if recaudacion > maxRecaudacion:
                maxRecaudacion = recaudacion
                mejorVendedor = vendedor

        if mejorVendedor:
            return f"{mejorVendedor.getNombre()} {mejorVendedor.getApellido()} ha recaudado un total de {maxRecaudacion} en ventas."
        else:
            return "No se encontró ningún mejor vendedor por recaudación."

    def crear_publicacion(self, producto, inventario_aleatorio, precio_aleatorio):
        self.publicaciones.append(Publicacion(self, producto, inventario_aleatorio, precio_aleatorio))


