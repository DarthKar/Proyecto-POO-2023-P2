import random
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from src.base_datos.comprador_repositorio import CompradorRepositorio

from src.base_datos.base_datos import BaseDatos
from src.base_datos.producto_repositorio import ProductoRepositorio
from src.base_datos.usuario_repositorio import UsuarioRepositorio
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.orden.orden import Orden
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.comprador import Comprador
from src.gestor_aplicacion.entidad.producto.producto import Producto
from src.gestor_aplicacion.entidad.producto.categoria import Categoria
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.membresia import Membresia
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.producto_transaccion import ProductoTransaccion
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.vendedor.vendedor import Vendedor
from src.uiMain.devolucion_field import DevolucionField
from src.uiMain.field_frame import FieldFrame
from src.uiMain.Comprador_field_principal import Comprador_principal
from tkinter import messagebox
from src.base_datos.repositorio import Repositorio
from src.uiMain.Estadisiticas_field_principal import Estadistica_field
from src.uiMain.Opinion_field_principal import opinion_principal
from src.gestor_aplicacion.entidad.usuario.usuario import Usuario


class Main:

    def CV(self):
        actual = self.listaCv.index(self.label_p2.cget("text"))
        cambio = (actual + 1) % len(self.listaCv)
        print(cambio)
        self.label_p2.config(text=self.listaCv[cambio])
        self.label_p2_fotos.config(image=self.listaImagenesCv[4*(cambio+1)-4])
        self.label_p3_fotos.config(image=self.listaImagenesCv[4*(cambio+1)-3])
        self.label_p4_fotos.config(image=self.listaImagenesCv[4*(cambio+1)-2])
        self.label_p5_fotos.config(image=self.listaImagenesCv[4*(cambio+1)-1])
        self.comprador = None



    # Evento de cambio de foto al pasar encima de la foto
    def iniciar_sesion(self):
        usuarioLB = self.entry_usuario.get()
        self.comprador = CompradorRepositorio.obtener_por_id(int(usuarioLB))

        if self.comprador is not None:

            messagebox.showinfo("Inicio de Sesión", f"Bienvenido, {self.comprador.getNombre()}!")
            # Si la autenticación es exitosa, ocultamos la ventana de inicio de sesión y mostramos la principal
            self.InicioSesion.withdraw()
            self.ventanaPrincipalI.deiconify()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def cambiar_imagenBienvenida(self):

        if not hasattr(self, 'cambio'):
            self.cambio = 0
        self.label_foto1.config(image=self.listaImagenesBienvenida[self.cambio])
        self.cambio += 1
        if self.cambio >= len(self.listaImagenesBienvenida):
            self.cambio = 0

    def ayuda(self):
        messagebox.showinfo("Creadores", "Miguel Angel Peña\nJuan Pablo Gaviria\nSebastian Gomez\nJuan Felipe Cadavid")

    def aplicacion(self):
        messagebox.showinfo("Choopi","La aplicacion busca ser un sistema de e-commerce completo. Esto incluye almacenar información de usuarios, gestionar productos (inventario, edición, agregado y eliminación), y permitir a los usuarios comprar, calificar productos y crear listas de deseos. El objetivo es modelar una tienda online con interacciones complejas entre clases para reflejar su funcionalidad de manera efectiva.")

    def cambioDeVentana(self):
        self.ventana.withdraw()
        self.InicioSesion.deiconify()

    def cambioDeVentanaSesion(self):
        self.InicioSesion.withdraw()
        self.ventanaPrincipalI.deiconify()
    # Evento volver ventana

    def volverVentana(self):
        self.ventanaPrincipalI.withdraw()
        self.ventana.deiconify()

    # Evento cambio de contenido en la ventana interfaz usuario

    def cambiarContenido(self, proceso):
        if proceso == "Compra":
            self.LabelDesc.config(text="Realizar Compra")
            self.LabelDesc2.config(
                text="El sistema de gestión de carrito de compras permite a los usuarios agregar, eliminar y gestionar los productos que desean comprar mientras navegan por la tienda en línea. Esta funcionalidad involucra múltiples objetos y componentes que interactúan para proporcionar una experiencia de compra fluida y coherente.",
                font=("arial", 10), wraplength=500)
            self.comprar()
        elif proceso == "Devolucion":
            self.LabelDesc.config(text="Realizar Devolución")
            self.LabelDesc2.config(text="Aquí va la descripción para realizar una devolución.")
            self.devolucion()
        elif proceso == "opinion":
            self.LabelDesc.config(text="Opinar", font=("YU Gothic","45"))
            self.LabelDesc2.config(text="El sistema de opiniones permite a los usuarios crear, editar y borrar a los usuarios opiniones de los productos y vendedores dentro de la tienda, esta funcionalidad permite la interaccion entre usuarios de la tienda para mejorar la experiencia general.",
                                   font=("arial", 10), wraplength=500)
            self.opinion()
        elif proceso == "Estadistica":
            self.LabelDesc.config(text="Estadística", font=("italic", "45"))
            self.LabelDesc2.config(text=" Aquí podras consultar las Estadisticas.", font=("italic", "25"))
            self.estadistica()



    # ------------------------------------------------------------------------------------------------------------------------

    # Carga de Imagenes para el CV

    def cargar_imagenes(self):
        tempList = []
        for i in range(0, len(self.listaCv)*2):
            tempList.append(ImageTk.PhotoImage(Image.open(f"src/{i + 1}.gif").resize((250, 225))))
        return tempList

    # Carga de Imagenes Ecommerce

    def cargar_imagenesBienvenida(self):
        tempListB = []
        for i in range(0, 5):
            tempListB.append(ImageTk.PhotoImage(Image.open(f"src/{i + 17}.gif").resize((250, 225))))
        return tempListB

# ------------------------------------------------------------------------------------------------

    def opinion(self):
        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        # Llama a FieldFrame con el número de campos deseado (por ejemplo, 3 campos)
        opc = [
        "Opinar sobre un producto",
        "Editar una opinion producto",
        "Borrar una opinion de un producto",
        "Opinar sobre un vendedor",
        "Editar una opinion vendedor",
        "Borrar una opinion de un vendedor"
         ]
        x = opinion_principal(self.FrameWidgets,"Opciones",opc,6,"Numero de referencia")
        x.crearPrincipal()
#------------------------------------------------------------------------------------------------

    def comprar(self):
        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        opciones = [
    "Mostrar lista de productos",
    "Agregar productos al carrito",
    "Eliminar productos del carrito",
    "Mostrar carrito",
    "Realizar pago",
    ]
        co = Comprador_principal(self.FrameWidgets,"Opciones",opciones,5,"Numero de referencia", self.comprador)
        co.crearPrincipal()


# ------------------------------------------------------------------------------------------------

    def estadistica(self):
        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        es = Estadistica_field(self.FrameWidgets,"Opciones","",0,"Numero de referencia")
        es.estadistica_principal()

# ------------------------------------------------------------------------------------------------
    def devolucion(self):

        orden = self.obtener_orden()

        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        opciones = [
             "1. Elegir productos a devolver"
                , "2. Deshacer productos a devolver"
                , "3. Listar productos a devolver"
                , "4. Guardar"
        ]
        co = DevolucionField(self.FrameWidgets, "Opciones", opciones, 4, "Numero de referencia", orden)
        co.crearPrincipal()

# ------------------------------------------------------------------------------------------------

    def __init__(self):

        # Establecimiento de Ventana Principal

        str(Comprador.MasCompradorValor())
        self.comprador = None
        self.ventana = tk.Tk()
        self.ventana.attributes('-fullscreen', True)
        self.ventana.title("Choopi")
        self.ventana.geometry("600x500")

        # Lista con los CV

        self.listaCv = [
            "Sebastian Gomez Zapata, 22 años, estudiante de la Universidad Nacional de Colombia sede Medellin de Ingenieria de Sistemas",
            "Miguel Angel Peña, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
            "Juan Pablo Gaviria Orozco, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
            "Juan Felipe Cadavid Ruiz, estudiante de Ingenieria de Sistemas e Informatica, Universidad Nacional de Colombia"
        ]

        # Se cargan las imagenes que se van a utilizar
        self.listaImagenesCv = self.cargar_imagenes()
        self.listaImagenesBienvenida = self.cargar_imagenesBienvenida()

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(0, weight=1)

        self.ventanaInicio = tk.Frame(self.ventana)
        self.ventanaInicio.pack(fill="both", expand=True)

        self.menuInicio = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menuInicio)

        # Creacion Menu Inicio

        self.menu1 = tk.Menu(self.menuInicio, font=("italic"), tearoff=0)
        self.menuInicio.add_cascade(label="Inicio", menu=self.menu1)
        self.menu1.add_command(label="Descripcion")
        self.menu1.add_separator()
        self.menu1.add_command(label="Salir", command=quit)

        self.framePrincipal = tk.Frame(self.ventanaInicio, bg="black")
        self.framePrincipal.pack(fill="both", expand=True, padx=10)

        self.p1 = tk.Frame(self.framePrincipal, bg="dark blue")
        self.p1.pack(side="left", padx=10, fill="both", expand=True)

        self.p2 = tk.Frame(self.framePrincipal, bg="black")
        self.p2.pack(side="right", padx=10, fill="both", expand=True)

        # CREACION FRAME CV

        self.p2_label_frame = tk.Frame(self.p2, bg="white")
        self.p2_label_frame.pack(side="top", padx=10, pady=10, fill="both", expand=True)
        self.label_p2 = tk.Label(self.p2_label_frame, text=self.listaCv[0], font=("italic", 25), bg="white",fg="black",
                                 wraplength=490)
        self.label_p2.grid(row=0, column=0)
        self.p2_label_frame.grid_rowconfigure(0, weight=1)
        self.p2_label_frame.grid_columnconfigure(0, weight=1)
        self.label_p2.bind("<Button-1>", lambda event: self.CV())
        self.p2_fotos_frame = tk.Frame(self.p2, bg="black")
        self.p2_fotos_frame.pack(pady=10, padx=10, fill="both", expand=True)

        img = Image.open("src/1.gif")
        resized_img = img.resize((250, 225))
        pil = ImageTk.PhotoImage(resized_img)
        img2 = Image.open("src/2.gif")
        resize2 = img2.resize((250, 225))

        pil2 = ImageTk.PhotoImage(resize2)
        img3 = Image.open("src/3.gif")
        resize3 = img3.resize((250, 225))

        pil3 = ImageTk.PhotoImage(resize3)

        img4 = Image.open("src/4.gif")
        resize4 = img4.resize((250, 225))

        pil4 = ImageTk.PhotoImage(resize4)

        self.label_p2_fotos = tk.Label(self.p2_fotos_frame, image=pil, )
        self.label_p2_fotos.grid(row=0, column=0, pady=5, padx=5, sticky="news")
        self.label_p3_fotos = tk.Label(self.p2_fotos_frame, image=pil2, )
        self.label_p3_fotos.grid(row=1, column=0, pady=5, padx=5, sticky="news")
        self.label_p4_fotos = tk.Label(self.p2_fotos_frame, image=pil3, )
        self.label_p4_fotos.grid(row=0, column=1, pady=5, padx=5, sticky="news")
        self.label_p5_fotos = tk.Label(self.p2_fotos_frame, image=pil4, )
        self.label_p5_fotos.grid(row=1, column=1, pady=5, padx=5, sticky="news")
        self.p2_fotos_frame.grid_rowconfigure(0, weight=1)
        self.p2_fotos_frame.grid_columnconfigure(0, weight=1)
        self.p2_fotos_frame.grid_rowconfigure(1, weight=1)
        self.p2_fotos_frame.grid_columnconfigure(1, weight=1)

        # FRAME BIENVENIDA
        self.p3 = tk.Frame(self.p1, bg="light blue")
        self.p3.pack(side="top", padx=10, pady=10, fill="both", expand=True)
        self.label_p3 = tk.Label(self.p3, text="¡Bienvenido a Choopi!", font=("italic", 55), bg="light blue",
                                 fg="black")
        self.label_p3.pack(pady=10)

        self.p4 = tk.Frame(self.p1, bg="light blue")
        self.p4.pack(padx=10, pady=10, fill="both", expand=True)
        self.label_foto1 = tk.Label(self.p4)
        foto1 = Image.open("src/18.gif").resize((400, 356))
        foto1 = ImageTk.PhotoImage(foto1)
        self.label_foto1.config(image=foto1, compound="bottom")
        self.label_foto1.image = foto1
        self.label_foto1.pack(pady=10, padx=10)
        botonVentanaUsuario = tk.Button(self.p4, text="Entrar a la tienda", padx=60, pady=45,
                                        command=self.cambioDeVentana, bg="light blue", fg="black", font=("Arial", 16),
                                        relief="raised", borderwidth=3, )
        botonVentanaUsuario.pack(side="bottom")
        self.label_foto1.bind("<Enter>",
                              lambda event: self.cambiar_imagenBienvenida())  # Evento cambio de imagen Frame Bienvenida

        # Ventana de Usuario Interfaz
        self.InicioSesion = tk.Toplevel()
        self.InicioSesion.title("Inicio de Sesión")
        self.InicioSesion.geometry("650x600")
        self.frameSesion = tk.Frame(self.InicioSesion, bg="light blue")
        self.frameSesion.pack(expand=True, fill="both")

        # Etiquetas y entradas para el nombre de usuario y la contraseña
        tk.Label(self.frameSesion, text="Usuario:").pack(pady=10)
        self.entry_usuario = tk.Entry(self.frameSesion)
        self.entry_usuario.pack(pady=10)

        tk.Label(self.frameSesion, text="Contraseña:").pack(pady=10)
        self.entry_contrasena = tk.Entry(self.frameSesion, show="*")
        self.entry_contrasena.pack(pady=10)

        # Botón para iniciar sesión
        self.boton_login = tk.Button(self.frameSesion, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_login.pack(pady=10)





        self.ventanaPrincipalI = tk.Toplevel()
        self.ventanaPrincipalI.title("choopi")
        self.ventanaPrincipalI.geometry("650x600")

        self.menuP = tk.Menu(self.ventanaPrincipalI, tearoff=0)
        self.ventanaPrincipalI.config(menu=self.menuP)

        # Menu archivo
        self.menuArchivo = tk.Menu(self.menuP, font=("italic"), tearoff=0)
        self.menuP.add_cascade(label="Archivo", menu=self.menuArchivo)
        self.menuArchivo.add_command(label="Aplicacion", command=self.aplicacion)
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Salir", command=self.volverVentana)

        # Menu funcionalidades
        self.MenuFuncionalidades = tk.Menu(self.menuP, font=("italic"), tearoff=0)
        self.menuP.add_cascade(label="Procesos y consultas", menu=self.MenuFuncionalidades)
        self.MenuFuncionalidades.add_command(label="Realizar Compra", command=lambda: self.cambiarContenido("Compra"))
        self.MenuFuncionalidades.add_command(label="Realizar Devolucion",
                                             command=lambda: self.cambiarContenido("Devolucion"))
        self.MenuFuncionalidades.add_command(label="Opinar", command=lambda: self.cambiarContenido("opinion"))
        self.MenuFuncionalidades.add_command(label="Estadistica", command=lambda: self.cambiarContenido("Estadistica"))
        self.menuP.add_command(label="ayuda", command=self.ayuda)

        self.frameContenedor = tk.Frame(self.ventanaPrincipalI, bg="light blue")
        self.frameContenedor.pack(fill="both", expand=True)

        self.frameDelLabelDesc = tk.Frame(self.frameContenedor)
        self.frameDelLabelDesc.pack(pady=10)
        self.LabelDesc = tk.Label(self.frameDelLabelDesc, text="a", bg="light blue", fg="black", font=("italic", 35),
                                  wraplength=270)
        self.LabelDesc.grid(row=0, column=0, columnspan=2)

        self.frameDelLabelDesc2 = tk.Frame(self.frameContenedor)
        self.frameDelLabelDesc2.pack(pady=10)
        self.LabelDesc2 = tk.Label(self.frameDelLabelDesc2, text="DESCRIPCION PROCESO O FUNCIONALIDAD", bg="light blue",
                                   fg="black", font=("italic", 25), wraplength=400)
        self.LabelDesc2 = tk.Label(self.frameDelLabelDesc2, text="DESCRIPCION PROCESO O FUNCIONALIDAD",
                                   font=("italic", 15),
                                   wraplength=400)
        self.LabelDesc2.grid(row=2, column=0, columnspan=4)

        self.FrameWidgets = tk.Frame(self.frameContenedor, bg="white")
        self.FrameWidgets.pack(pady=10)
        self.cambiarContenido("Compra")

        self.ventanaPrincipalI.withdraw()
        self.InicioSesion.withdraw()
        self.ventana.mainloop()

    def obtener_orden(self):
        # Crear una nueva ventana Toplevel
        ventana = tk.Toplevel(self.ventanaPrincipalI)
        ventana.title("Selecciona la orden")

        # Crear un Combobox en la ventana Toplevel
        combo = ttk.Combobox(ventana, values=list(map(lambda orden: F"{orden.getId()}", self.comprador.getOrdenes())))
        combo.pack(padx=10, pady=10)

        # Función para manejar el botón OK
        seleccion = tk.StringVar()
        def on_ok():
            if(combo.get() is None or combo.get() == ""):
                return
            seleccion.set(combo.get())
            ventana.destroy()

        # Botón OK para cerrar la ventana Toplevel
        btn_ok = tk.Button(ventana, text="OK", command=on_ok)
        btn_ok.pack(pady=10)

        # Hacer que la ventana principal se bloquee mientras la ventana Toplevel está abierta
        self.ventanaPrincipalI.wait_window(ventana)
        return self.comprador.get_orden_por_id(int(seleccion.get()))




def valores_por_defecto():
    productos = []
    compradores = []
    vendedores = []

    productos.append(Producto(2, "Televisor", Categoria.ELECTRONICA))
    productos.append(Producto(1, "Ron", Categoria.ALIMENTOS))
    productos.append(Producto(3, "Pomada", Categoria.ROPA))
    productos.append(Producto(4, "Sofá", Categoria.HOGAR))
    productos.append(Producto(5, "Muñeca", Categoria.JUGUETES))
    productos.append(Producto(6, "Crema facial", Categoria.COSMETICOS))
    productos.append(Producto(7, "Libro", Categoria.OTROS))
    productos.append(Producto(8, "Desinfectante", Categoria.ELECTRONICA))
    productos.append(Producto(9, "Cepillo de dientes", Categoria.HOGAR))
    productos.append(Producto(10, "Manzanas", Categoria.ALIMENTOS))
    productos.append(Producto(11, "Lámpara", Categoria.HOGAR))
    productos.append(Producto(12, "Pantalones", Categoria.ROPA))
    productos.append(Producto(13, "Chocolate", Categoria.ALIMENTOS))
    productos.append(Producto(14, "Teléfono móvil", Categoria.ELECTRONICA))
    productos.append(Producto(15, "Pelota de fútbol", Categoria.JUGUETES))
    productos.append(Producto(16, "Champú", Categoria.COSMETICOS))
    productos.append(Producto(17, "Taza", Categoria.HOGAR))
    productos.append(Producto(18, "Reloj", Categoria.ELECTRONICA))
    productos.append(Producto(19, "Camiseta polo", Categoria.ROPA))
    productos.append(Producto(20, "Impresora", Categoria.ALIMENTOS))
    productos.append(Producto(21, "Consola de videojuegos", Categoria.ELECTRONICA))
    productos.append(Producto(22, "Toallas", Categoria.HOGAR))
    productos.append(Producto(23, "Maquillaje", Categoria.COSMETICOS))
    productos.append(Producto(24, "Peluche", Categoria.JUGUETES))
    productos.append(Producto(25, "Libreta", Categoria.OTROS))
    productos.append(Producto(26, "Silla", Categoria.HOGAR))
    productos.append(Producto(27, "Gafas de sol", Categoria.OTROS))
    productos.append(Producto(28, "Pasta de dientes", Categoria.HOGAR))
    productos.append(Producto(29, "Café", Categoria.ALIMENTOS))
    productos.append(Producto(30, "Perfume", Categoria.COSMETICOS))
    productos.append(Producto(31, "Arroz", Categoria.ALIMENTOS))
    productos.append(Producto(32, "Camiseta", Categoria.ROPA))
    productos.append(Producto(33, "Teléfono", Categoria.ELECTRONICA))
    productos.append(Producto(34, "Leche", Categoria.ALIMENTOS))
    productos.append(Producto(35, "Portátil", Categoria.ELECTRONICA))
    compradores.append(Comprador(1, "Pedro", "Moreno", "pedro@example.com", Membresia.ORO, 234))
    compradores.append(Comprador(2, "Ana", "López", "ana@example.com", Membresia.PLATA, 456))
    compradores.append(Comprador(3, "Juan", "Gómez", "juan@example.com", Membresia.BASICA, 123))
    compradores.append(Comprador(4, "María", "Rodríguez", "maria@example.com", Membresia.BRONCE, 67))
    compradores.append(Comprador(5, "Sofía", "Martínez", "sofia@example.com", Membresia.NINGUNA, 87))
    compradores.append(Comprador(6, "Carlos", "Pérez", "carlos@example.com", Membresia.ORO, 89))
    compradores.append(Comprador(7, "Laura", "Fernández", "laura@example.com", Membresia.PLATA, 122))
    compradores.append(Comprador(8, "Diego", "Hernández", "diego@example.com", Membresia.BASICA, 111))
    compradores.append(Comprador(9, "Isabel", "Díaz", "isabel@example.com", Membresia.BRONCE, 102))
    compradores.append(Comprador(10, "Luis", "García", "luis@example.com", Membresia.NINGUNA, 334))
    compradores.append(Comprador(11, "Alejandro", "González", "alejandro@example.com", Membresia.ORO, 34))
    compradores.append(Comprador(12, "Elena", "Torres", "elena@example.com", Membresia.PLATA, 12))
    compradores.append(Comprador(13, "Miguel", "Ruiz", "miguel@example.com", Membresia.BASICA, 34))
    compradores.append(Comprador(14, "Carmen", "Sánchez", "carmen@example.com", Membresia.BRONCE, 345))
    compradores.append(Comprador(15, "Andrea", "Lara", "andrea@example.com", Membresia.NINGUNA, 234))
    compradores.append(Comprador(16, "Ricardo", "Vargas", "ricardo@example.com", Membresia.ORO, 123))
    compradores.append(Comprador(17, "Natalia", "Pérez", "natalia@example.com", Membresia.PLATA, 103))
    compradores.append(Comprador(18, "Daniel", "Gómez", "daniel@example.com", Membresia.BASICA, 167))
    compradores.append(Comprador(19, "Lucía", "Hernández", "lucia@example.com", Membresia.BRONCE, 178))
    compradores.append(Comprador(20, "Javier", "Soto", "javier@example.com", Membresia.NINGUNA, 78))
    compradores.append(Comprador(21, "Natalia", "López", "natalia@example.com", Membresia.PLATA, 789))
    compradores.append(Comprador(22, "Pablo", "Martínez", "pablo@example.com", Membresia.BASICA, 56))
    compradores.append(Comprador(23, "Valeria", "Gutiérrez", "valeria@example.com", Membresia.BRONCE, 90))
    compradores.append(Comprador(24, "Sara", "Jiménez", "sara@example.com", Membresia.NINGUNA, 89))
    compradores.append(Comprador(25, "Juan", "Torres", "juan@example.com", Membresia.ORO, 123))
    compradores.append(Comprador(26, "María", "Gómez", "maria@example.com", Membresia.PLATA, 78))
    compradores.append(Comprador(27, "Lucas", "Díaz", "lucas@example.com", Membresia.BASICA, 86))
    compradores.append(Comprador(28, "Valentina", "Fernández", "valentina@example.com", Membresia.BRONCE, 126))
    compradores.append(Comprador(29, "Gabriel", "Pérez", "gabriel@example.com", Membresia.NINGUNA, 67))
    compradores.append(Comprador(30, "Sofía", "Moreno", "sofia@example.com", Membresia.ORO, 456))
    compradores.append(Comprador(31, "Pedro", "Moreno", "pedro@example.com", Membresia.ORO, 678))
    compradores.append(Comprador(32, "Ana", "González", "ana@example.com", Membresia.PLATA, 90))
    compradores.append(Comprador(33, "Juan", "López", "juan@example.com", Membresia.BRONCE, 145))
    compradores.append(Comprador(34, "María", "Sánchez", "maria@example.com", Membresia.ORO, 167))
    compradores.append(Comprador(35, "Luis", "Martínez", "luis@example.com", Membresia.PLATA, 189))
    compradores.append(Comprador(36, "Aristobulo", "Cachimbo", "aristi@example.com", Membresia.ORO, 78))
    compradores.append(Comprador(37, "Apolo", "Cachimbo", "apolo@example.com", Membresia.ORO, 78))
    compradores.append(Comprador(38, "Roberto", "Gómez", "roberto@example.com"))
    compradores.append(Comprador(39, "Luciana", "Hernández", "luciana@example.com"))
    compradores.append(Comprador(40, "Carlos", "Pérez", "carlos@example.com"))
    compradores.append(Comprador(41, "Elena", "Díaz", "elena@example.com"))
    compradores.append(Comprador(42, "Gustavo", "Fernández", "gustavo@example.com"))
    compradores.append(Comprador(43, "Verónica", "Martínez", "veronica@example.com"))
    compradores.append(Comprador(44, "Jorge", "García", "jorge@example.com"))
    compradores.append(Comprador(45, "Fernanda", "López", "fernanda@example.com"))
    compradores.append(Comprador(46, "Federico", "Sánchez", "federico@example.com"))
    compradores.append(Comprador(47, "Silvana", "Torres", "silvana@example.com"))
    vendedores.append(Vendedor(1, "Juan", "Pérez", "juan@example.com"))
    vendedores.append(Vendedor(2, "María", "López", "maria@example.com"))
    vendedores.append(Vendedor(3, "Carlos", "Gómez", "carlos@example.com"))
    vendedores.append(Vendedor(4, "Ana", "Martínez", "ana@example.com"))
    vendedores.append(Vendedor(5, "Laura", "Sánchez", "laura@example.com"))
    vendedores.append(Vendedor(6, "Pedro", "Fernández", "pedro@example.com"))
    vendedores.append(Vendedor(7, "Sofía", "Hernández", "sofia@example.com"))
    vendedores.append(Vendedor(8, "Diego", "Díaz", "diego@example.com"))
    vendedores.append(Vendedor(9, "Isabel", "Gutiérrez", "isabel@example.com"))
    vendedores.append(Vendedor(10, "Luis", "Torres", "luis@example.com"))
    vendedores.append(Vendedor(11, "Elena", "Ruiz", "elena@example.com"))
    vendedores.append(Vendedor(12, "Miguel", "Soto", "miguel@example.com"))
    vendedores.append(Vendedor(13, "Carmen", "Lara", "carmen@example.com"))
    vendedores.append(Vendedor(14, "Andrea", "Jiménez", "andrea@example.com"))
    vendedores.append(Vendedor(15, "Ricardo", "Vargas", "ricardo@example.com"))
    vendedores.append(Vendedor(16, "Natalia", "Gómez", "natalia@example.com"))
    vendedores.append(Vendedor(17, "Daniel", "Pérez", "daniel@example.com"))
    vendedores.append(Vendedor(18, "Lucía", "Moreno", "lucia@example.com"))
    vendedores.append(Vendedor(19, "Gabriel", "Martínez", "gabriel@example.com"))
    vendedores.append(Vendedor(20, "Valentina", "Sánchez", "valentina@example.com"))
    vendedores.append(Vendedor(21, "Alejandro", "Gómez", "alejandro@example.com"))
    vendedores.append(Vendedor(22, "Pablo", "López", "pablo@example.com"))
    vendedores.append(Vendedor(23, "Valeria", "Torres", "valeria@example.com"))
    vendedores.append(Vendedor(24, "Sara", "Hernández", "sara@example.com"))
    vendedores.append(Vendedor(25, "Juan", "Díaz", "juan@example.com"))
    vendedores.append(Vendedor(26, "María", "Gutiérrez", "maria@example.com"))
    vendedores.append(Vendedor(27, "Lucas", "Fernández", "lucas@example.com"))
    vendedores.append(Vendedor(28, "Natalia", "Pérez", "natalia@example.com"))
    vendedores.append(Vendedor(29, "Sofía", "Moreno", "sofia@example.com"))
    vendedores.append(Vendedor(30, "Javier", "Soto", "javier@example.com"))
    vendedores.append(Vendedor(31, "Juan", "Pérez"))
    vendedores.append(Vendedor(32, "María", "García"))
    vendedores.append(Vendedor(33, "Carlos", "López"))
    vendedores.append(Vendedor(34, "Ana", "Martínez"))
    vendedores.append(Vendedor(35, "Pedro", "Sánchez"))
    for vendedor in vendedores:
        cantidad_publicaciones = random.randint(10, 20)
        for i in range(1, cantidad_publicaciones):
            while True:
                try:
                    producto_aleatorio = random.randint(0, len(productos) - 1)
                    inventario_aleatorio = random.randint(1, 99)
                    precio_aleatorio = random.uniform(10, 100)
                    vendedor.crear_publicacion(productos[producto_aleatorio], inventario_aleatorio,
                                               precio_aleatorio)
                    break
                except ValueError as e:
                    print(f"Error: {e}")
                    break

    for comprador in compradores:
        cantidad_ordenes = random.randint(1, 9)
        for i in range(cantidad_ordenes):
            orden = Orden(i, comprador)
            cantidad_articulos = random.randint(1, 4)
            for j in range(cantidad_articulos):
                producto_aleatorio = random.randint(0, len(productos) - 1)
                producto = productos[producto_aleatorio]
                publicacion_aleatoria = random.randint(0, len(producto.getPublicaciones()) - 1)
                publicacion = producto.getPublicaciones()[publicacion_aleatoria]
                cantidad_aleatoria = random.randint(1, 10)
                producto_transaccion = ProductoTransaccion(publicacion, cantidad_aleatoria)
                orden.agregar_producto(producto_transaccion)
            comprador.agregar_orden(orden)
    base_datos = BaseDatos()
    base_datos.set_productos(productos)
    base_datos.set_vendedores(vendedores)
    base_datos.set_compradores(compradores)
    return base_datos

if Repositorio.crear_directorio() or Repositorio.crear_archivo():
    Repositorio.leer(valores_por_defecto())
else:
    Repositorio.leer(None)

app = Main()
