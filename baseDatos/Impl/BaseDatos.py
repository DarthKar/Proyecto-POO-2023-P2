import pickle
from gestorAplicacion.entidad.Producto import Categoria
from gestorAplicacion.entidad.Producto import Producto
from gestorAplicacion.entidad.Usuario.tiposDeUsuario import Vendedor
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.Membresia import Membresia
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador import Comprador

class BaseDatos:
    def __init__(self):
        compradores = []
        vendedores = []
        productos = []
    
    def getCompradores(self):
        return self.compradores

    def getProductos(self):
        return self.productos
    
    def getVendedores(self):
        return self.vendedores
    
    def setCompradores(self, compradores):
        self.compradores = compradores
    
    def setProductos(self, productos):
        self.productos = productos

    def setVendedores(self, vendedores):
        self.vendedores = vendedores
    
    
    def valoresPorDefecto(self):
        self.productos.append(Producto(1, "Ron", Categoria.ALIMENTOS))
        self.productos.append(Producto(2, "Televisor", Categoria.ELECTRONICA))
        self.productos.approductosend(Producto(3, "Pomada", Categoria.ROPA))
        self.productos.append(Producto(4, "Sofá", Categoria.HOGAR))
        self.productos.append(Producto(5, "Muñeca", Categoria.JUGUETES))
        self.productos.approductos
        self.productos.append(Producto(7, "Libro", Categoria.OTROS))
        self.productos.append(Producto(8, "Desinfectante", Categoria.ELECTRONICA))
        self.productos.append(Producto(9, "Cepillo de dientes", Categoria.HOGAR))
        self.productos.append(Producto(10, "Manzanas", Categoria.ALIMENTOS))
        self.productos.append(Producto(11, "Lámpara", Categoria.HOGAR))
        self.productos.append(Producto(12, "Pantalones", Categoria.ROPA))
        self.productos.append(Producto(13, "Chocolate", Categoria.ALIMENTOS))
        self.productos.append(Producto(14, "Teléfono móvil", Categoria.ELECTRONICA))
        self.productos.append(Producto(15, "Pelota de fútbol", Categoria.JUGUETES))
        self.productos.append(Producto(16, "Champú", Categoria.COSMETICOS))
        self.productos.append(Producto(17, "Taza", Categoria.HOGAR))
        self.productos.append(Producto(18, "Reloj", Categoria.ELECTRONICA))
        self.productos.append(Producto(19, "Camiseta polo", Categoria.ROPA))
        self.productos.append(Producto(20, "Impresora", Categoria.ALIMENTOS))
        self.productos.append(Producto(21, "Consola de videojuegos", Categoria.ELECTRONICA))
        self.productos.append(Producto(22, "Toallas", Categoria.HOGAR))
        self.productos.append(Producto(23, "Maquillaje", Categoria.COSMETICOS))
        self.productos.append(Producto(24, "Peluche", Categoria.JUGUETES))
        self.productos.append(Producto(25, "Libreta", Categoria.OTROS))
        self.productos.append(Producto(26, "Silla", Categoria.HOGAR))
        self.productos.append(Producto(27, "Gafas de sol", Categoria.OTROS))
        self.productos.append(Producto(28, "Pasta de dientes", Categoria.HOGAR))
        self.productos.append(Producto(29, "Café", Categoria.ALIMENTOS))
        self.productos.append(Producto(30, "Perfume", Categoria.COSMETICOS))
        self.productos.append(Producto(31, "Arroz", Categoria.ALIMENTOS))
        self.productos.append(Producto(32, "Camiseta", Categoria.ROPA))
        self.productos.append(Producto(33, "Teléfono", Categoria.ELECTRONICA))
        self.productos.append(Producto(34, "Leche", Categoria.ALIMENTOS))
        self.productos.append(Producto(35, "Portátil", Categoria.ELECTRONICA))

        self.compradores.append(Comprador(1, "Pedro", "Moreno", "pedro@example.com", Membresia.ORO, 234))
        self.compradores.append(Comprador(2, "Ana", "López", "ana@example.com", Membresia.PLATA, 456))
        self.compradores.append(Comprador(3, "Juan", "Gómez", "juan@example.com", Membresia.BASICA, 123))
        self.compradores.append(Comprador(4, "María", "Rodríguez", "maria@example.com", Membresia.BRONCE, 67))
        self.compradores.append(Comprador(5, "Sofía", "Martínez", "sofia@example.com", Membresia.NINGUNA, 87))
        self.compradores.append(Comprador(6, "Carlos", "Pérez", "carlos@example.com", Membresia.ORO, 89))
        self.compradores.append(Comprador(7, "Laura", "Fernández", "laura@example.com", Membresia.PLATA, 122))
        self.compradores.append(Comprador(8, "Diego", "Hernández", "diego@example.com", Membresia.BASICA, 111))
        self.compradores.append(Comprador(9, "Isabel", "Díaz", "isabel@example.com", Membresia.BRONCE, 102))
        self.compradores.append(Comprador(10, "Luis", "García", "luis@example.com", Membresia.NINGUNA, 334))
        self.compradores.append(Comprador(11, "Alejandro", "González", "alejandro@example.com", Membresia.ORO, 34))
        self.compradores.append(Comprador(12, "Elena", "Torres", "elena@example.com", Membresia.PLATA, 12))
        self.compradores.append(Comprador(13, "Miguel", "Ruiz", "miguel@example.com", Membresia.BASICA, 34))
        self.compradores.append(Comprador(14, "Carmen", "Sánchez", "carmen@example.com", Membresia.BRONCE, 345))
        self.compradores.append(Comprador(15, "Andrea", "Lara", "andrea@example.com", Membresia.NINGUNA, 234))
        self.compradores.append(Comprador(16, "Ricardo", "Vargas", "ricardo@example.com", Membresia.ORO, 123))
        self.compradores.append(Comprador(17, "Natalia", "Pérez", "natalia@example.com", Membresia.PLATA, 103))
        self.compradores.append(Comprador(18, "Daniel", "Gómez", "daniel@example.com", Membresia.BASICA, 167))
        self.compradores.append(Comprador(19, "Lucía", "Hernández", "lucia@example.com", Membresia.BRONCE, 178))
        self.compradores.append(Comprador(20, "Javier", "Soto", "javier@example.com", Membresia.NINGUNA, 78))
        self.compradores.append(Comprador(21, "Natalia", "López", "natalia@example.com", Membresia.PLATA, 789))
        self.compradores.append(Comprador(22, "Pablo", "Martínez", "pablo@example.com", Membresia.BASICA, 56))
        self.compradores.append(Comprador(23, "Valeria", "Gutiérrez", "valeria@example.com", Membresia.BRONCE, 90))
        self.compradores.append(Comprador(24, "Sara", "Jiménez", "sara@example.com", Membresia.NINGUNA, 89))
        self.compradores.append(Comprador(25, "Juan", "Torres", "juan@example.com", Membresia.ORO, 123))
        self.compradores.append(Comprador(26, "María", "Gómez", "maria@example.com", Membresia.PLATA, 78))
        self.compradores.append(Comprador(27, "Lucas", "Díaz", "lucas@example.com", Membresia.BASICA, 86))
        self.compradores.append(Comprador(28, "Valentina", "Fernández", "valentina@example.com", Membresia.BRONCE, 126))
        self.compradores.append(Comprador(29, "Gabriel", "Pérez", "gabriel@example.com", Membresia.NINGUNA, 67))
        self.compradores.append(Comprador(30, "Sofía", "Moreno", "sofia@example.com", Membresia.ORO, 456))
        self.compradores.append(Comprador(31, "Pedro", "Moreno", "pedro@example.com", Membresia.ORO, 678))
        self.compradores.append(Comprador(32, "Ana", "González", "ana@example.com", Membresia.PLATA, 90))
        self.compradores.append(Comprador(33, "Juan", "López", "juan@example.com", Membresia.BRONCE, 145))
        self.compradores.append(Comprador(34, "María", "Sánchez", "maria@example.com", Membresia.ORO, 167))
        self.compradores.append(Comprador(35, "Luis", "Martínez", "luis@example.com", Membresia.PLATA, 189))
        self.compradores.append(Comprador(36, "Aristobulo", "Cachimbo", "aristi@example.com", Membresia.ORO, 78))
        self.compradores.append(Comprador(37, "Aristobulo", "Cachimbo", "aristi@example.com", Membresia.ORO, 78))
        self.compradores.append(Comprador(38, "Roberto", "Gómez", "roberto@example.com"))
        self.compradores.append(Comprador(39, "Luciana", "Hernández", "luciana@example.com"))
        self.compradores.append(Comprador(40, "Carlos", "Pérez", "carlos@example.com"))
        self.compradores.append(Comprador(41, "Elena", "Díaz", "elena@example.com"))
        self.compradores.append(Comprador(42, "Gustavo", "Fernández", "gustavo@example.com"))
        self.compradores.append(Comprador(43, "Verónica", "Martínez", "veronica@example.com"))
        self.compradores.append(Comprador(44, "Jorge", "García", "jorge@example.com"))
        self.compradores.append(Comprador(45, "Fernanda", "López", "fernanda@example.com"))
        self.compradores.append(Comprador(46, "Federico", "Sánchez", "federico@example.com"))
        self.compradores.append(Comprador(47, "Silvana", "Torres", "silvana@example.com"))

        self.vendedores.append(Vendedor(1, "Juan", "Pérez", "juan@example.com"))
        self.vendedores.append(Vendedor(2, "María", "López", "maria@example.com"))
        self.vendedores.append(Vendedor(3, "Carlos", "Gómez", "carlos@example.com"))
        self.vendedores.append(Vendedor(4, "Ana", "Martínez", "ana@example.com"))
        self.vendedores.append(Vendedor(5, "Laura", "Sánchez", "laura@example.com"))
        self.vendedores.append(Vendedor(6, "Pedro", "Fernández", "pedro@example.com"))
        self.vendedores.append(Vendedor(7, "Sofía", "Hernández", "sofia@example.com"))
        self.vendedores.append(Vendedor(8, "Diego", "Díaz", "diego@example.com"))
        self.vendedores.append(Vendedor(9, "Isabel", "Gutiérrez", "isabel@example.com"))
        self.vendedores.append(Vendedor(10, "Luis", "Torres", "luis@example.com"))
        self.vendedores.append(Vendedor(11, "Elena", "Ruiz", "elena@example.com"))
        self.vendedores.append(Vendedor(12, "Miguel", "Soto", "miguel@example.com"))
        self.vendedores.append(Vendedor(13, "Carmen", "Lara", "carmen@example.com"))
        self.vendedores.append(Vendedor(14, "Andrea", "Jiménez", "andrea@example.com"))
        self.vendedores.append(Vendedor(15, "Ricardo", "Vargas", "ricardo@example.com"))
        self.vendedores.append(Vendedor(16, "Natalia", "Gómez", "natalia@example.com"))
        self.vendedores.append(Vendedor(17, "Daniel", "Pérez", "daniel@example.com"))
        self.vendedores.append(Vendedor(18, "Lucía", "Moreno", "lucia@example.com"))
        self.vendedores.append(Vendedor(19, "Gabriel", "Martínez", "gabriel@example.com"))
        self.vendedores.append(Vendedor(20, "Valentina", "Sánchez", "valentina@example.com"))
        self.vendedores.append(Vendedor(21, "Alejandro", "Gómez", "alejandro@example.com"))
        self.vendedores.append(Vendedor(22, "Pablo", "López", "pablo@example.com"))
        self.vendedores.append(Vendedor(23, "Valeria", "Torres", "valeria@example.com"))
        self.vendedores.append(Vendedor(24, "Sara", "Hernández", "sara@example.com"))
        self.vendedores.append(Vendedor(25, "Juan", "Díaz", "juan@example.com"))
        self.vendedores.append(Vendedor(26, "María", "Gutiérrez", "maria@example.com"))
        self.vendedores.append(Vendedor(27, "Lucas", "Fernández", "lucas@example.com"))
        self.vendedores.append(Vendedor(28, "Natalia", "Pérez", "natalia@example.com"))
        self.vendedores.append(Vendedor(29, "Sofía", "Moreno", "sofia@example.com"))
        self.vendedores.append(Vendedor(30, "Javier", "Soto", "javier@example.com"))
        self.vendedores.append(Vendedor(31, "Juan", "Pérez"))
        self.vendedores.append(Vendedor(32, "María", "García"))
        self.vendedores.append(Vendedor(33, "Carlos", "López"))
        self.vendedores.append(Vendedor(34, "Ana", "Martínez"))
        self.vendedores.append(Vendedor(35, "Pedro", "Sánchez"))

        #Falta copiar la implementaciones ramdom.....