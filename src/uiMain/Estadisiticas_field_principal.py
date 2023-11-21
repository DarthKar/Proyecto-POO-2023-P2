import tkinter as tk
from tkinter import messagebox
from src.uiMain.field_frame import FieldFrame
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.comprador import Comprador
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.vendedor.vendedor import Vendedor
from src.gestor_aplicacion.entidad.producto.producto import Producto

class Estadistica_field(FieldFrame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores=None, habilitado=None):
        super().__init__(master,tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores, habilitado)
        for widget in self.winfo_children():
            widget.destroy()
    
     # Metodo mas comprador
    def funcionalidadMasComprador(self):
        # Basicamente aca esta el llamado a todos los metodos
        messagebox.showinfo("Estadistica", str(Comprador.mas_comprador()) )

    # Metodo factura mas alta
    def funcionalidadCompradoFactura(self):

        messagebox.showinfo("Estadistica", str(Comprador.MasCompradorValor()) )

    # Metodo membresia mas comun
    def funcionalidadMembresia(self):

        messagebox.showinfo("Estadistica", str(Comprador.membresia_mas_comprada()))

    # Metodo Ventas Totales
    def funcionalidadVentasTotales(self):

        messagebox.showinfo("Estadistica", str(Producto.ventasTotales()) )

    # Metodo Total Productos vendidos
    def funcionalidadTotalProductosVendidos(self):

        messagebox.showinfo("Estadistica",str(Producto.productosTotalesVendidos()) )

    # Metodo Mas Vendedor
    def funcionalidadMasVendedor(self):

        messagebox.showinfo("Estadistica", str(Vendedor.mejorVendendor()))

    # Metodo Mas recaudador
    def funcionalidadMasRecaudador(self):

        messagebox.showinfo("Estadistica", str(Vendedor.mejorVendedorPorRecaudacion()))

    # Metodo Producto Mas Caro
    def funcionalidadMasCaro(self):

        messagebox.showinfo("Estadistica", "El producto mas caro es la ropa")

    # Metodo Producto mas Barato
    def funcionalidadMasBarato(self):

        messagebox.showinfo("Estadistica", str(Producto.productoMasBarato()))

    # Metodo Mas Vendido
    def funcionalidadTotalMasVendido(self):

        messagebox.showinfo("Estadistica", "El producto mas vendido son los celulares")
        
    def estadistica_principal(self):
        self.frameEstadisticas = tk.Frame(self, bg="black")
        self.frameEstadisticas.pack()
        # Funcionalidad mas comprador
        labelUsuario = tk.Label(self.frameEstadisticas, text="Usuario que más productos compró", bg="black", fg="white",
                                font=("italic", "18"))
        labelUsuario.grid(row=0, column=0, columnspan=4)
        labelUsuario.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasComprador, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=0, column=5, columnspan=2)
        # Funcionalidad mas comprador por factura
        labelComprador = tk.Label(self.frameEstadisticas, text="Usuario con la factura mas alta", bg="black", fg="white",
                                  font=("italic", "18"))
        labelComprador.grid(row=1, column=0, columnspan=4)
        labelComprador.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadCompradoFactura, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=1, column=5, columnspan=2)
        # Funcionalidad membresia mas Usada
        labelMembresia = tk.Label(self.frameEstadisticas, text="La membresia mas comprada", bg="black",fg="white",
                                  font=("italic", "18"))
        labelMembresia.grid(row=2, column=0, columnspan=4)
        labelMembresia.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMembresia, height=3, fg="white",
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=2, column=5, columnspan=2)
        # Funcionalidad Ventas Totales
        labelVentasTotales = tk.Label(self.frameEstadisticas, text="Ventas totales del E-commerce", bg="black", fg="white",
                                      font=("italic", "18"))
        labelVentasTotales.grid(row=3, column=0, columnspan=4)
        labelVentasTotales.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadVentasTotales, height=3,
                          width=20)
        boton.columnconfigure(3, weight=1)
        boton.grid(row=3, column=5, columnspan=2)
        # Total Productos vendidos
        labelProductosVendidos = tk.Label(self.frameEstadisticas, text="Total productos Vendidos", bg="black", fg="white",
                                          font=("italic", "18"))
        labelProductosVendidos.grid(row=4, column=0, columnspan=4)
        labelProductosVendidos.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadTotalProductosVendidos,
                          height=3, width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=4, column=5, columnspan=2)
        # Mas Vendedor
        labelProductosVendidos = tk.Label(self.frameEstadisticas, text="Usuario que mas vendió", bg="black", fg="white",
                                          font=("italic", "18"))
        labelProductosVendidos.grid(row=5, column=0, columnspan=4)
        labelProductosVendidos.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasVendedor, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=5, column=5, columnspan=2)
        # Mas Recaudo
        labelProductosVendidos = tk.Label(self.frameEstadisticas, text="El vendedor com mayor recaudo", bg="black", fg="white",
                                          font=("italic", "18"))
        labelProductosVendidos.grid(row=6, column=0, columnspan=4)
        labelProductosVendidos.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasRecaudador, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=6, column=5, columnspan=2)
        # Producto mas Caro
        labelProductosVendidos = tk.Label(self.frameEstadisticas, text="Producto mas caro", bg="black", fg="white",
                                          font=("italic", "18"))
        labelProductosVendidos.grid(row=7, column=0, columnspan=4)
        labelProductosVendidos.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasCaro, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=7, column=5, columnspan=2)
        # Producto mas Barato
        labelProductosVendidos = tk.Label(self.frameEstadisticas, text="El producto mas Barato", bg="black", fg="white",
                                          font=("italic", "18"))
        labelProductosVendidos.grid(row=8, column=0, columnspan=4)
        labelProductosVendidos.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadMasBarato, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=8, column=5, columnspan=2)
        # Total Producto Mas vendido
        labelProductosVendidos = tk.Label(self.frameEstadisticas, text="El producto mas Vendido", bg="black", fg="white",
                                          font=("italic", "18"))
        labelProductosVendidos.grid(row=9, column=0, columnspan=4)
        labelProductosVendidos.columnconfigure(0, weight=1)
        boton = tk.Button(self.frameEstadisticas, text="Botón", command=self.funcionalidadTotalMasVendido, height=3,
                          width=20)
        boton.columnconfigure(1, weight=1)
        boton.grid(row=9, column=5, columnspan=2)