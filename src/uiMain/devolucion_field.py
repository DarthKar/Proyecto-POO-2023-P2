import tkinter as tk
from tkinter import messagebox

from src.excepciones.excepciones import ValidacionDevolucionError, OrdenError, DevolucionError, \
    InventarioDevolucionError
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.orden.devolucion import Devolucion
from src.gestor_aplicacion.entidad.usuario.tiposDeUsuario.comprador.producto_transaccion import ProductoTransaccion
from src.uiMain.field_frame import FieldFrame


class DevolucionField(FieldFrame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, orden, valores=None,
                 habilitado=None):
        super().__init__(master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores, habilitado)
        self.orden = orden
        self.productosDevolucion = []
        for widget in self.winfo_children():
            widget.destroy()

    def crearPrincipal(self):

        # Crear la ventana principal
        if self.habilitado is None:
            self.habilitado = [False] * self.cantidad_campos

        if self.valores is None:
            self.valores = [""] * self.cantidad_campos

        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio, font=("Arial", 10))
        label_titulo_criterio.grid(row=0, column=0, columnspan=6, sticky="w")

        label_titulo_valores = tk.Label(self, text=self.tituloValores, font=("Arial", 10))  # Interfaz principal
        label_titulo_valores.grid(row=0, column=6, columnspan=6, sticky="w")

        for i in range(self.cantidad_campos):
            label_criterio = tk.Label(self, text=f"{self.nombres_criterios[i]}")
            label_criterio.grid(row=i + 1, column=0, columnspan=6, sticky="w")

            entry_value = tk.StringVar()
            entry_value.set(str(i + 1))
            entry = tk.Entry(self, state="readonly", textvariable=entry_value, justify='center')
            entry.insert(0, self.valores[i])
            entry.grid(row=i + 1, column=6, columnspan=6, sticky="w")

        self.entrada_usuario = tk.Entry(self, state="normal", justify='center')
        self.entrada_usuario.insert(0, "Ingrese un numero")
        self.entrada_usuario.bind("<FocusIn>", self.limpiarTextos)
        self.entrada_usuario.grid(row=self.cantidad_campos + 2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

        self.boton_aceptar = tk.Button(self, text="enviar", command=self.Opciones)
        self.boton_aceptar.grid(row=self.cantidad_campos + 2, column=6, columnspan=6, padx=10, pady=10, sticky="w")

    # -----------------------------------------------------------------------------------------

    def limpiarTextos(self, event):

        if self.entrada_usuario.get() == "Ingrese un numero":
            self.entrada_usuario.delete(0, tk.END)

            # -----------------------------------------------------------------------------------------

    # Primera opcion

    def volver_principal(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.crearPrincipal()

    def interfaz_1(self, label_1):
        for idx, texto in enumerate(label_1):
            fila = idx % 9
            columna = idx // 9

            lab = tk.Label(self, text=texto, borderwidth=1, relief="solid")
            lab.grid(row=fila, column=columna, padx=5, pady=5, sticky="w")

        # Botón de regresar al final
        boton_regresar = tk.Button(self, text="continuar", bg="#3BA8F9", command=self.interfaz_1_2)
        boton_regresar.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    # -----------------------------------------------------------------------------------------

    def interfaz_1_2(self):
        for widget in self.winfo_children():
            widget.destroy()
        label_producto = tk.Label(self, text="Elija una publicación que desea devolver", justify="center")
        label_producto.grid(row=0, column=0)

        entry_producto = tk.Entry(self, width=30)
        entry_producto.grid(row=0, column=1)

        label_unidades = tk.Label(self, text="¿Cuántas unidades desea devolver?", justify="center")
        label_unidades.grid(row=1, column=0)

        entry_unidades = tk.Entry(self, width=30)
        entry_unidades.grid(row=1, column=1)

        boton_seguir = tk.Button(self, text="seguir", bg="#3BA8F9",
                                 command=lambda: self.interfaz_1_3(entry_producto.get(), entry_unidades.get()))
        boton_seguir.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    # -----------------------------------------------------------------------------------------

    def interfaz_1_3(self, publicacion, cantidad):

        try:
            if (not publicacion.isdigit() or publicacion == "" or int(publicacion) <= 0):
                raise ValidacionDevolucionError("Ingrese en publicación un número válido")
            if (not cantidad.isdigit() or cantidad == "" or int(cantidad) <= 0):
                raise ValidacionDevolucionError("Ingrese en cantidad un número válido")
            if (int(publicacion) > len(self.orden.getProductosTransaccion())):
                raise OrdenError("Ha seleccionado una publicación no valida.")

            pt = self.orden.getProductosTransaccion()[int(publicacion) - 1]

            if(int(cantidad) > pt.getPublicacion().getInventario()):
                raise InventarioDevolucionError(F"Ha seleccionado una cantidad invalida. No puede ser mayor que {pt.cantidad()}")

            self.productosDevolucion.append(
                ProductoTransaccion(pt.getPublicacion(), int(cantidad)))

        except DevolucionError as e:
            messagebox.showerror('Error', str(e.get_mensaje()))
            self.interfaz_1_2()

        self.confirmacion("Se ha agregado publicacion a devolver con exito")

    def confirmacion(self, texto, boolean=True):
        for widget in self.winfo_children():
            widget.destroy()
        confirmacion_label = tk.Label(self, text=texto)
        confirmacion_label.grid(row=0, column=0, padx=5, pady=5)
        if (boolean):
            boton_regresar = tk.Button(self, text="Regresar", bg="#3BA8F9", command=self.volver_principal)
            boton_regresar.grid(row=1, column=0)

    def interfaz_2(self, label_1):
        self.productosDevolucion = []
        self.confirmacion("Se ha limpiado los productos a devolver")

    # -----------------------------------------------------------------------------------------

    def interfaz_3(self, label_1):
        for idx, texto in enumerate(label_1):
            fila = idx % 9
            columna = idx // 9

            lab = tk.Label(self, text=texto, borderwidth=1, relief="solid")
            lab.grid(row=fila, column=columna, padx=5, pady=5, sticky="w")

        # Botón de regresar al final
        boton_regresar = tk.Button(self, text="Regresar", bg="#3BA8F9", command=self.volver_principal)
        boton_regresar.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    def interfaz_4(self):
        devolucion = Devolucion(len(self.orden.getComprador().getOrdenes()), self.orden.getComprador(), self.orden)
        for item in self.productosDevolucion:
            devolucion.agregar_producto(item)
        self.orden.getComprador().agregarDevolucion(devolucion)

        self.confirmacion("Se ha guardado correctamente la devolución", False)

    def Opciones(self):
        elegido = self.entrada_usuario.get()

        def validar_entrada():
            try:
                opcion = int(elegido)
                if (opcion < 1) or (opcion > 11):
                    raise ValidacionDevolucionError("El número debe estar entre 1 y 11")
                if not elegido.isdigit():
                    raise ValidacionDevolucionError("Cuidado!", "Ingrese un número válido entre 1 y 11")
                if elegido == "":
                    raise ValidacionDevolucionError("Cuidado!", "Ingrese un número válido")
                return True
            except ValidacionDevolucionError as e:
                messagebox.showinfo("Cuidado!", e.get_mensaje())
                return False

        if not validar_entrada():
            return
            # ---------------------------------------------------------------
        if elegido == "1":
            for widget in self.winfo_children():
                widget.destroy()
            pro = []
            num = 1
            for i in self.orden.getProductosTransaccion():
                pro.append(f"{num}. {i.getPublicacion().getProducto().getNombre()} - Cantidad {i.getCantidad()}")
                num = num + 1
            self.interfaz_1(pro)

        if elegido == "2":
            for widget in self.winfo_children():
                widget.destroy()
            self.interfaz_2(pro)

        if elegido == "3":
            pu = []
            num = 1
            for i in self.orden.getProductosTransaccion():
                pu.append(f"{num}. {i.getPublicacion().getProducto().getNombre()} - Cantidad {i.getCantidad()}")
                num = num + 1

            for widget in self.winfo_children():
                widget.destroy()
            self.interfaz_3(pu)

        if elegido == "4":
            for widget in self.winfo_children():
                widget.destroy()
            self.interfaz_4()