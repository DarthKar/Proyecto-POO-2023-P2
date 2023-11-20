import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.uiMain.field_frame import FieldFrame
from src.uiMain.Comprador_field_principal import Comprador_principal
#from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.comprador import Comprador
from tkinter import messagebox

class Main:
    #Evento de cambio de Curriculum

    def CV(self):
        actual = self.listaCv.index(self.label_p2.cget("text"))
        cambio = (actual + 1) % len(self.listaCv)
        self.label_p2.config(text=self.listaCv[cambio])
        self.label_p3_fotos.config(image=self.listaImagenesCv[cambio])
        self.label_p4_fotos.config(image=self.listaImagenesCv[cambio+1])
        self.label_p5_fotos.config(image=self.listaImagenesCv[cambio])
        self.label_p2_fotos.config(image=self.listaImagenesCv[cambio])
        
    
    #Evento de cambio de foto al pasar encima de la foto

    def cambiar_imagenBienvenida(self):

        if not hasattr(self, 'cambio'):
            self.cambio = 0
        self.label_foto1.config(image=self.listaImagenesBienvenida[self.cambio])
        self.cambio += 1
        if self.cambio >= len(self.listaImagenesBienvenida):
            self.cambio = 0
            

    def ayuda(self):
        messagebox.showinfo("Creadores", "Miguel Angel Peña\nJuan Pablo Gaviria\nSebastian Gomez\nJuan Felipe Cadavid")

    #Evento cambio de ventana

    def cambioDeVentana(self):
        self.ventana.withdraw()
        self.ventanaPrincipalI.deiconify()

    #Evento volver ventana

    def volverVentana(self):
        self.ventanaPrincipalI.withdraw()
        self.ventana.deiconify()

    #Evento cambio de contenido en la ventana interfaz usuario
    
    def cambiarContenido(self, proceso):
        if proceso == "Compra":
            self.LabelDesc.config(text="Realizar Compra")
            self.LabelDesc2.config(text="El sistema de gestión de carrito de compras permite a los usuarios agregar, eliminar y gestionar los productos que desean comprar mientras navegan por la tienda en línea. Esta funcionalidad involucra múltiples objetos y componentes que interactúan para proporcionar una experiencia de compra fluida y coherente.",font = ("arial",10),wraplength=500)
            self.comprar()
        elif proceso == "Devolucion":
            self.LabelDesc.config(text="Realizar Devolución")
            self.LabelDesc2.config(text="Aquí va la descripción para realizar una devolución.")
        elif proceso == "opinion":
            self.LabelDesc.config(text="Opinar")
            self.LabelDesc2.config(text="Aquí va la descripción para dejar una opinión.")
            self.opinion()
        elif proceso == "Estadistica":
            self.LabelDesc.config(text="Estadística",font=("italic","45"))
            self.LabelDesc2.config(text=" Aquí podras consultar las Estadisticas.",font=("italic","25"))
            self.FrameWidgets.pack_forget()
            self.frameEstadisticas=tk.Frame(self.frameContenedor,bg="black")
            self.frameEstadisticas.pack()

            #Funcionalidad mas comprador

            labelUsuario = tk.Label(self.frameEstadisticas, text="Usuario que más productos compró",bg="black",font=("italic","18"))
            labelUsuario.grid(row=0,column=0,columnspan=4)
            labelUsuario.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasComprador,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=0,column=5,columnspan=2)
            
            # Funcionalidad mas comprador por factura

            labelComprador = tk.Label(self.frameEstadisticas, text="Usuario con la factura mas alta",bg="black",font=("italic","18"))
            labelComprador.grid(row=1,column=0,columnspan=4)
            labelComprador.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadCompradoFactura,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=1,column=5,columnspan=2)
            
            # Funcionalidad membresia mas Usada

            labelMembresia = tk.Label(self.frameEstadisticas, text="La membresia mas comprada",bg="black",font=("italic","18"))
            labelMembresia.grid(row=2,column=0,columnspan=4)
            labelMembresia.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMembresia,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=2,column=5,columnspan=2)

            # Funcionalidad Ventas Totales

            labelVentasTotales = tk.Label(self.frameEstadisticas, text="Ventas totales del E-commerce",bg="black",font=("italic","18"))
            labelVentasTotales.grid(row=3,column=0,columnspan=4)
            labelVentasTotales.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadVentasTotales,height=3, width=20)
            boton.columnconfigure(3,weight=1)
            boton.grid(row=3,column=5,columnspan=2)

            # Total Productos vendidos

            labelProductosVendidos = tk.Label(self.frameEstadisticas, text="Total productos Vendidos",bg="black",font=("italic","18"))
            labelProductosVendidos.grid(row=4,column=0,columnspan=4)
            labelProductosVendidos.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadTotalProductosVendidos,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=4,column=5,columnspan=2)

            # Mas Vendedor

            labelProductosVendidos = tk.Label(self.frameEstadisticas, text="Usuario que mas vendió",bg="black",font=("italic","18"))
            labelProductosVendidos.grid(row=5,column=0,columnspan=4)
            labelProductosVendidos.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasVendedor,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=5,column=5,columnspan=2)

            # Mas Recaudo

            labelProductosVendidos = tk.Label(self.frameEstadisticas, text="El vendedor com mayor recaudo",bg="black",font=("italic","18"))
            labelProductosVendidos.grid(row=6,column=0,columnspan=4)
            labelProductosVendidos.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasRecaudador,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=6,column=5,columnspan=2)

            # Producto mas Caro

            labelProductosVendidos = tk.Label(self.frameEstadisticas, text="Producto mas caro",bg="black",font=("italic","18"))
            labelProductosVendidos.grid(row=7,column=0,columnspan=4)
            labelProductosVendidos.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasCaro,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=7,column=5,columnspan=2)

            # Producto mas Barato

            labelProductosVendidos = tk.Label(self.frameEstadisticas, text="El producto mas Barato",bg="black",font=("italic","18"))
            labelProductosVendidos.grid(row=8,column=0,columnspan=4)
            labelProductosVendidos.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasBarato,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=8,column=5,columnspan=2)

            # Total Producto Mas vendido

            labelProductosVendidos = tk.Label(self.frameEstadisticas, text="El producto mas Vendido",bg="black",font=("italic","18"))
            labelProductosVendidos.grid(row=9,column=0,columnspan=4)
            labelProductosVendidos.columnconfigure(0,weight=1)
            boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadTotalMasVendido,height=3, width=20)
            boton.columnconfigure(1,weight=1)
            boton.grid(row=9,column=5,columnspan=2)

    #  ****  Definicion de metodos de la funcionalidad estadistica ****

    #Metodo mas comprador
    def funcionalidadMasComprador(self):
        #Basicamente aca esta el llamado a todos los metodos
        messagebox.showinfo("Estadistica","El usuario mas comprador es pepito perez")
    
    #Metodo factura mas alta
    def funcionalidadCompradoFactura(self):
        
        messagebox.showinfo("Estadistica","El usuario con la factura mas alta es peranito")
    
    #Metodo membresia mas comun
    def funcionalidadMembresia(self):
        
        messagebox.showinfo("Estadistica","La membresia mas comun es Oro")

    #Metodo Ventas Totales
    def funcionalidadVentasTotales(self):
        
        messagebox.showinfo("Estadistica","El E-commerce genero en total 2000")
    
    #Metodo Total Productos vendidos
    def funcionalidadTotalProductosVendidos(self):
        
        messagebox.showinfo("Estadistica","En total se vendieron 15 productos")

    #Metodo Mas Vendedor
    def funcionalidadMasVendedor(self):
        
        messagebox.showinfo("Estadistica","El mas vendedor fue Cristiano Ronaldo")
    
    #Metodo Mas recaudador
    def funcionalidadMasRecaudador(self):
        
        messagebox.showinfo("Estadistica","El vendedor que mas Recaudo es Messi")
    
    #Metodo Producto Mas Caro
    def funcionalidadMasCaro(self):
        
        messagebox.showinfo("Estadistica","El producto mas caro es la ropa")

    #Metodo Producto mas Barato
    def funcionalidadMasBarato(self):
        
        messagebox.showinfo("Estadistica","El producto mas barato es la sal")

    #Metodo Mas Vendido
    def funcionalidadTotalMasVendido(self):
        
        messagebox.showinfo("Estadistica","El producto mas vendido son los celulares")


    #Carga de Imagenes para el CV

    def cargar_imagenes(self):
        tempList = []
        for i in range(0, len(self.listaCv)):
            tempList.append(ImageTk.PhotoImage(Image.open(f"src/{i + 1}.gif").resize((250, 225))))
        return tempList
    
   #Carga de Imagenes Ecommerce
   
    def cargar_imagenesBienvenida(self):
        tempListB = []
        for i in range(0, 5):
            tempListB.append(ImageTk.PhotoImage(Image.open(f"src/{i + 17}.gif").resize((250, 225))))
        return tempListB

#------------------------------------------------------------------------------------------------

    def opinion(self):
        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        # Llama a FieldFrame con el número de campos deseado (por ejemplo, 3 campos)
        FieldFrame(self.FrameWidgets, "Datos",["ID", "Comentario", "Valoracion"], 3, "Introduce aqui los datos")

#------------------------------------------------------------------------------------------------
    
    def comprar(self):
        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        opciones = [
    "Mostrar lista de productos",
    "Agregar productos recomendados al carrito",
    "Agregar productos al carrito",
    "Eliminar productos del carrito",
    "Mostrar carrito",
    "Modificar carrito",
    "Modificar informacion de pago",
    "Crear orden de compra",
    "Realizar pago",
    "Vaciar ordenes de pago",
    "Ver ordenes de pago",
    "Volver al menu principal"
    ]
        Comprador_principal(self.FrameWidgets,"Opciones",opciones,12,"Numero de referencia")
        
#------------------------------------------------------------------------------------------------

    def __init__(self):
        
        #Establecimiento de Ventana Principal
        
        self.ventana = tk.Tk()
        self.ventana.attributes('-fullscreen', True)
        self.ventana.title("Choopi")
        self.ventana.geometry("600x500")

        #Lista con los CV

        self.listaCv = [
            "Sebastian Gomez Zapata, 22 años, estudiante de la Universidad Nacional de Colombia sede Medellin de Ingenieria de Sistemas",
            "Miguel Angel Peña, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
            "Juan Pablo Gaviria Orozco, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
            "Juan Felipe Cadavid Ruiz, estudiante de Ingenieria de Sistemas e Informatica, Universidad Nacional de Colombia"
        ]

        #Se cargan las imagenes que se van a utilizar
        self.listaImagenesCv = self.cargar_imagenes()
        self.listaImagenesBienvenida = self.cargar_imagenesBienvenida()

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(0, weight=1)

        self.ventanaInicio = tk.Frame(self.ventana)
        self.ventanaInicio.pack(fill="both", expand=True)

        self.menuInicio = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menuInicio)

        #Creacion Menu Inicio
        
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

        #CREACION FRAME CV

        self.p2_label_frame = tk.Frame(self.p2, bg="white")
        self.p2_label_frame.pack(side="top", padx=10, pady=10,fill="both", expand=True)
        self.label_p2 = tk.Label(self.p2_label_frame, text=self.listaCv[0], font=("italic", 25), bg="white",wraplength=490)
        self.label_p2.grid(row=0, column=0) 
        self.p2_label_frame.grid_rowconfigure(0, weight=1)
        self.p2_label_frame.grid_columnconfigure(0, weight=1)
        self.label_p2.bind("<Button-1>", lambda event: self.CV())
        self.p2_fotos_frame = tk.Frame(self.p2, bg="black")
        self.p2_fotos_frame.pack(pady=10,padx=10,fill="both",expand=True)

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

        #FRAME BIENVENIDA
        self.p3 = tk.Frame(self.p1, bg="light blue")
        self.p3.pack(side="top", padx=10, pady=10, fill="both", expand=True)
        self.label_p3 = tk.Label(self.p3, text="¡Bienvenido a Choopi!", font=("italic", 55),bg="light blue",fg="black")
        self.label_p3.pack(pady=10)

        self.p4 = tk.Frame(self.p1, bg="light blue")
        self.p4.pack(padx=10, pady=10, fill="both", expand=True)
        self.label_foto1 = tk.Label(self.p4)
        foto1 = Image.open("src/18.gif").resize((400, 356))
        foto1 = ImageTk.PhotoImage(foto1)
        self.label_foto1.config(image=foto1, compound="bottom")
        self.label_foto1.image = foto1
        self.label_foto1.pack(pady=10, padx=10)
        botonVentanaUsuario = tk.Button(self.p4, text="usuario interfaz", padx=60, pady=45, command=self.cambioDeVentana,bg="light blue",fg="black",  font=("Arial", 16),relief="raised", borderwidth=3,)
        botonVentanaUsuario.pack(side="bottom")
        self.label_foto1.bind("<Enter>", lambda event: self.cambiar_imagenBienvenida())   #Evento cambio de imagen Frame Bienvenida

     
        #Ventana de Usuario Interfaz
        
        self.ventanaPrincipalI = tk.Toplevel()
        self.ventanaPrincipalI.title("choopi")
        self.ventanaPrincipalI.geometry("600x500")

        self.menuP = tk.Menu(self.ventanaPrincipalI, tearoff=0)
        self.ventanaPrincipalI.config(menu=self.menuP)

        #Menu archivo
        self.menuArchivo = tk.Menu(self.menuP, font=("italic"), tearoff=0)
        self.menuP.add_cascade(label="Archivo", menu=self.menuArchivo)
        self.menuArchivo.add_command(label="Aplicacion")
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Salir", command=self.volverVentana)

        #Menu funcionalidades
        self.MenuFuncionalidades = tk.Menu(self.menuP, font=("italic"), tearoff=0)
        self.menuP.add_cascade(label="Procesos y consultas", menu=self.MenuFuncionalidades)
        self.MenuFuncionalidades.add_command(label="Realizar Compra", command=lambda: self.cambiarContenido("Compra"))
        self.MenuFuncionalidades.add_command(label="Realizar Devolucion", command=lambda: self.cambiarContenido("Devolucion"))
        self.MenuFuncionalidades.add_command(label="Opinar", command=lambda: self.cambiarContenido("opinion"))
        self.MenuFuncionalidades.add_command(label="Estadistica", command=lambda: self.cambiarContenido("Estadistica"))
        self.menuP.add_command(label="ayuda", command=self.ayuda)

        self.frameContenedor = tk.Frame(self.ventanaPrincipalI, bg="light blue")
        self.frameContenedor.pack(fill="both", expand=True)

        
        self.frameDelLabelDesc = tk.Frame(self.frameContenedor)
        self.frameDelLabelDesc.pack(pady=10)
        self.LabelDesc = tk.Label(self.frameDelLabelDesc, text="a", bg="light blue",fg="black", font=("italic", 35), wraplength=270)
        self.LabelDesc.grid(row=0, column=0, columnspan=2)

        self.frameDelLabelDesc2 = tk.Frame(self.frameContenedor)
        self.frameDelLabelDesc2.pack(pady=10)
        self.LabelDesc2 = tk.Label(self.frameDelLabelDesc2, text="DESCRIPCION PROCESO O FUNCIONALIDAD",bg="light blue",fg="black",font=("italic", 25),wraplength=400)
        self.LabelDesc2.grid(row=2, column=0, columnspan=4)

        self.FrameWidgets = tk.Frame(self.frameContenedor, bg="white")
        self.FrameWidgets.pack(pady=10)
        self.cambiarContenido("Compra")

        self.ventanaPrincipalI.withdraw()
        
        self.ventana.mainloop()


app = Main()
