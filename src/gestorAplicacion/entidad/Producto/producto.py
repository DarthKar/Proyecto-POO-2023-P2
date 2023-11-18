from collections import defaultdict
from src.baseDatos.Impl.CompradorRepositorio import CompradorRepositorio
from src.gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.Membresia import Membresia


class Producto:
    def __init__(self,id,nombre,categoria):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        _opinion = []
        _compradores = []
        _publicaciones = []
        _resenadores = []

        def addopinionProducto(resena):
            if resena is not None:
                _opinion.append(resena)
        
        def existeResena(comprador):
            return comprador in self._resenadores
        
        def getId(self):
            return self.id
        
        def getNombre(self):
            return self.nombre
        
        def getCategoria(self):
            return self.categoria
        
        def getopiniones(self):
            return self._opinion
        
        def getPublicaciones(self):
            return self._publicaciones
        
        def agregarPublicacion(self,publicacion):
            _publicaciones.append(publicacion)
        
        def setId(self,id):
            self.id = id
        
        def setNombre(self,nombre):
            self.nombre = nombre
        
        def setCategoria(self,categoria):
            self.categoria = categoria
        
        def setcompradores(self,compradores):
            self._compradores = compradores
        
        def get_compradores(self):
            return self._compradores
        
        def getresenadores(self):
            return self._resenadores

        def setopinion(self,opinion):
            self._opinion = opinion
        
        def setcompradores(self,compradores):
            self._compradores = compradores
        
        def setresenadores(self,resenadores):
            self._resenadores = resenadores
        
        def is_perecedero(self):
            return self.categoria.perecedero

        def agregarComprador(self,comprador):
            _compradores.append(comprador)
        
        @staticmethod
        def agregarResenador(cls,resenador):
            cls._resenadores.append(resenador)

        @staticmethod
        def producto_mas_vendido(cls):
            productos = defaultdict(int)

            for comprador in CompradorRepositorio.obtener():
                for orden in comprador.get_ordenes():  # Cambiar por transaccion
                    for producto_transaccion in orden.get_productos_transaccion():
                        producto = producto_transaccion.get_publicacion().get_producto()
                        productos[producto] += 1

            producto_mas_vendido = None
            valor = 0

            for producto, cantidad in productos.items():
                if cantidad > valor:
                    valor = cantidad
                    producto_mas_vendido = producto

            return producto_mas_vendido

        @staticmethod
        def productoMasCaro(cls):
            productoMasCaro = 0
            productoCaro = None
            for comprador in CompradorRepositorio.obtener():
                for orden in comprador.get_ordenes():
                    for productoTransaccion in orden.getProductosTransaccion():
                        if productoMasCaro < productoTransaccion.getPublicacion().getPrecio():
                            productoMasCaro = productoTransaccion.getPublicacion().getPrecio()
                            productoCaro=productoTransaccion.getPublicacion().getProducto().getNombre()
            return (productoMasCaro+" que vale "+productoCaro)
        
        @staticmethod
        def ventasTotales(cls):
            valorVentas = 0
            for comprador in CompradorRepositorio.obtener():
                for orden in comprador.getOrdenes():
                    for productoTransaccion in orden.getProductosTransaccion():
                        valorVentas += (productoTransaccion.getPublicacion().getPrecio()*productoTransaccion.getCantidad())
            return valorVentas

        @staticmethod
        def productosTotalesVendidos(cls):
            valorVendidos = 0
            for comprador in CompradorRepositorio.obtener():
                for orden in comprador.getOrdenes():
                    for productoTransaccion in orden.getProductosTransaccion():
                        valorVendidos += 1
            return valorVendidos
        
        @staticmethod
        def productoMasBarato(cls):
            productoMasBarato = float('inf')
            productoBarato = None

            for comprador in CompradorRepositorio.obtener():
                for orden in comprador.get_ordenes():
                    for productoTransaccion in orden.getProductosTransaccion():
                        if productoMasBarato > productoTransaccion.getPublicacion().getPrecio():
                            productoMasBarato = productoTransaccion.getPublicacion().getPrecio()
                            productoBarato = productoTransaccion.getPublicacion().getProducto().getNombre()

            return f"{productoBarato} que vale {productoMasBarato}"

        @staticmethod
        def membresia_mas_comprada(cls):
            Ninguna = 0
            Basica = 0
            Bronce = 0
            Plata = 0
            Oro = 0         
            for comprador in CompradorRepositorio.obtener():
                comparar = comprador.getMembresia()   
                if comparar == Membresia.NINGUNA : 
                    Ninguna += 1   
                elif comparar == Membresia.BASICA :
                    Basica += 1 
                elif comparar == Membresia.BRONCE:
                    Bronce +=1
                elif comparar == Membresia.PLATA:
                    Plata += 1
                elif comparar == Membresia.ORO:
                    Oro += 1	
            
            #Membresia mas comun
            membresiaMasComun = Membresia.NINGUNA
            maxCompras = Ninguna

            if (Basica > maxCompras):
                membresiaMasComun = Membresia.BASICA
                maxCompras = Basica
            elif (Bronce > maxCompras):
                membresiaMasComun = Membresia.BRONCE
                maxCompras = Bronce
            elif (Plata > maxCompras):
                membresiaMasComun = Membresia.PLATA
                maxCompras = Plata
            elif (Oro > maxCompras):
                membresiaMasComun = Membresia.ORO
	        
            return membresiaMasComun    

        @staticmethod
        def cantidadProductosVendidos(cls):
            productosDiferentes = set()
            for comprador in CompradorRepositorio.obtener():
                for orden in comprador.getOrdenes():
                    for productoTransaccion in orden.getProductosTransaccion():
                        producto = productoTransaccion.getPublicacion().getProducto()
                        productosDiferentes.append(producto)
            return len(productosDiferentes)


