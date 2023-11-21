from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.orden.carrito import Carrito
from src.base_datos.comprador_repositorio import CompradorRepositorio
from src.gestor_aplicacion.entidad.usuario.usuario import Usuario
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.membresia import Membresia
from collections import defaultdict
from operator import itemgetter
from src.base_datos.producto_repositorio import ProductoRepositorio
from collections import Counter



class Comprador(Usuario):
    def __init__(self, id, nombre, apellido, correo, membresia=Membresia.NINGUNA, saldo=100):
        super().__init__(id, nombre, apellido, correo)
        self._membresia = membresia
        self._saldo = saldo
        self._ordenes = []  
        self._devoluciones = []  
        self._resenasDeProductos = []
        self._productosComprados = []
        self._carrito = Carrito(id, self)

    def agregarProductoComprado(self,productoComprado):
        self._productosComprados.append(productoComprado)
    
    def getResenasDeProductos(self):
        return self._resenasDeProductos
    
    def getMembresia(self):
        return self._membresia
    
    def getOrdenes(self):
        return self._ordenes
   
    def obtenerCompradores(self):
        return CompradorRepositorio.obtenerCompradores

    def agregarDevolucion(self, devolucion):
        if not devolucion.getProductosTransaccion():  
            self._saldo += self.AplicarDescuento(devolucion.calcularTotal())
            self._devoluciones.append(devolucion)
            CompradorRepositorio.guardar(self)
    
    def getCarrito(self):
        return self._carrito
    
    def getSaldo(self):
        return self._saldo

    def quitarSaldo(self,quitar):
        self._saldo = self._saldo - quitar
    
    def agregarSaldo(self,dinero):
        self._saldo = self._saldo+dinero
    
    def AplicarDescuento(self, total_puro):
        a = 0
        if self._membresia == Membresia.NINGUNA:
            a = total_puro
        if self._membresia == Membresia.BASICA:
            a = total_puro * Membresia.PRECIO_BASICA  # método para aplicar los descuentos al total de una orden al ejecutar el pago
        if self._membresia == Membresia.BRONCE:
            a = total_puro * Membresia.PRECIO_BRONCE
        if self._membresia == Membresia.PLATA:
            a = total_puro * Membresia.PRECIO_PLATA
        if self._membresia == Membresia.ORO:
            a = total_puro * Membresia.PRECIO_ORO
        return a

    def mostrar_informacion(self):
        return f"Nombre: {self.getNombre()} {self.apellido}\nCorreo: {self.correo}\nTipo de Membresia: {self._membresia}\nSaldo: {self._saldo}"


    @staticmethod
    def obtenerCompradorPorId(_id):
        comprador = CompradorRepositorio.obtener_por_id(_id)
        if comprador is not None:
            return comprador
        else:
            raise ValueError(f"Comprador con id {_id} no ha sido encontrado.")

    def agregar_orden(self, orden):
        self._ordenes.append(orden)

    def getOrdenesValidasParaDevolucion(self):
        return [
            orden for orden in self._ordenes
            if not orden.isTieneDevoluciones() and orden.isPagar()
            and any(
                not productoTransaccion.getPublicacion().getProducto().getCategoria().isPerecedero()
                for productoTransaccion in orden.getProductosTransaccion()
            )
        ]


    @staticmethod
    def MasCompradorValor():
        comprasValorMaximo = 0
        masComprador = None

        for comprador in CompradorRepositorio.obtener():
            comprasValor = 0

            for orden in comprador.getOrdenes():
                for productosTransaccion in orden.getProductosTransaccion():
                    comprasValor += productosTransaccion.getPublicacion().getPrecio()

            if comprasValor > comprasValorMaximo:
                comprasValorMaximo = comprasValor
                masComprador = comprador

        if masComprador:
            return f"{masComprador.getNombre()} {masComprador.getApellido()} ha realizado compras por un valor máximo de {comprasValorMaximo}"
       
        else:
            return "No se encontró comprador con valor máximo de compras"

    @staticmethod
    def mas_comprador():

        tamanoOrdenes = 0
        masComprador = None

        for comprador in CompradorRepositorio.obtener():
            if len(comprador.getOrdenes()) > tamanoOrdenes:
                tamanoOrdenes = len(comprador.getOrdenes())
                masComprador = comprador

        if masComprador:
            return f"{masComprador.getNombre()} {masComprador.getApellido()} con el ID {masComprador.getId()} y con el correo electrónico {masComprador.getCorreo()} con un total de {tamanoOrdenes} productos comprados"
        else:
            return "No se encontró comprador con órdenes"


    def get_publicaciones_recomendadas(self,numero_publicaciones):
        if not self._ordenes:
            return []

        cantidad_de_compras_productos = defaultdict(int)
        cantidad_de_compras_publicacion = defaultdict(int)
        cantidad_de_compras_categoria = defaultdict(int)
        cantidad_de_compras_vendedor = defaultdict(int)

        publicaciones_adquiridas = [
            producto_transaccion.getPublicacion()
            for orden in self._ordenes
            for producto_transaccion in orden.getProductosTransaccion()
        ]

        for publicacion in publicaciones_adquiridas:
            producto = publicacion.getProducto()
            categoria = producto.getCategoria()
            vendedor = publicacion.getVendedor()

            cantidad_de_compras_vendedor[vendedor] += 1
            cantidad_de_compras_categoria[categoria] += 1
            cantidad_de_compras_publicacion[publicacion] += 1
            cantidad_de_compras_productos[producto] += 1

        ultima_orden = self._ordenes[-1]

        productos_mas_comprados = sorted(
            cantidad_de_compras_productos.keys(),
            key=cantidad_de_compras_productos.get,
            reverse=True
        )[:3]

        publicaciones_mas_compradas = sorted(
            cantidad_de_compras_publicacion.keys(),
            key=cantidad_de_compras_publicacion.get,
            reverse=True
        )[:3]

        vendedores_mas_comprados = sorted(
            cantidad_de_compras_vendedor.keys(),
            key=cantidad_de_compras_vendedor.get,
            reverse=True
        )[:3]

        categorias_mas_compradas = sorted(
            cantidad_de_compras_categoria.keys(),
            key=cantidad_de_compras_categoria.get,
            reverse=True
        )[:3]

        puntuacion_publicaciones = {}

        for producto in ProductoRepositorio.getProductos():
            puntuacion_producto = 0
            temp_publicaciones = {}

            for publicacion in producto.getPublicaciones():
                puntuacion_publicacion = 0

                if publicacion.getVendedor() in vendedores_mas_comprados:
                    puntuacion_publicacion += 5

                if publicacion in publicaciones_mas_compradas:
                    puntuacion_publicacion += 10

                if any(
                    producto_transaccion.getPublicacion() == publicacion
                    for producto_transaccion in ultima_orden.getProductosTransaccion()
                ):
                    puntuacion_publicacion += 4

                temp_publicaciones[publicacion] = puntuacion_publicacion

            if producto.getCategoria() in categorias_mas_compradas:
                puntuacion_producto += 5

            if producto in productos_mas_comprados:
                puntuacion_producto += 10

            publicacion_recomendada = max(
                temp_publicaciones.items(),
                key=itemgetter(1),
                default=(None, 0)
            )

            if publicacion_recomendada[0] is not None:
                puntuacion_publicaciones[publicacion_recomendada[0]] = (
                    puntuacion_producto + publicacion_recomendada[1]
                )

        return sorted(
            puntuacion_publicaciones.keys(),
            key=puntuacion_publicaciones.get,
            reverse=True
        )[:numero_publicaciones]
    
    @staticmethod
    def membresia_mas_comprada():
        compradores = CompradorRepositorio.obtener()
        contador_membresias = Counter(comprador.getMembresia() for comprador in compradores)

        membresia_mas_comun = max(contador_membresias, key=contador_membresias.get)

        return membresia_mas_comun
 
    