import select
import tkinter as tk
from tkinter import messagebox
from src.uiMain.field_frame import FieldFrame
from src.base_datos.producto_repositorio import ProductoRepositorio
from src.base_datos.usuario_repositorio import UsuarioRepositorio
from src.gestor_aplicacion.entidad.producto.producto import Producto

class Comprador_principal(FieldFrame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores=None, habilitado=None):
        super().__init__(master,tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores, habilitado)
        for widget in self.winfo_children():
            widget.destroy()
        
        
    def crearPrincipal(self):
        if self.habilitado is None:
            self.habilitado = [False] * self.cantidad_campos

        if self.valores is None:
            self.valores = [""] * self.cantidad_campos

        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio, font=("Arial", 10))
        label_titulo_criterio.grid(row=0, column=0, columnspan=6, sticky="w")

        label_titulo_valores = tk.Label(self, text=self.tituloValores, font=("Arial", 10))      #Interfaz principal
        label_titulo_valores.grid(row=0, column=6, columnspan=6, sticky="w")

        for i in range(self.cantidad_campos):
            label_criterio = tk.Label(self, text=f"{self.nombres_criterios[i]}")
            label_criterio.grid(row=i + 1, column=0, columnspan=6, sticky="w")

            entry_value = tk.StringVar()
            entry_value.set(str(i + 1))
            entry = tk.Entry(self, state="readonly",textvariable=entry_value,justify='center')
            entry.insert(0, self.valores[i])
            entry.grid(row=i + 1, column=6, columnspan=6, sticky="w")
        
        
        self.entrada_usuario = tk.Entry(self,state="normal",justify='center')
        self.entrada_usuario.insert(0,"Ingrese un numero")
        self.entrada_usuario.bind("<FocusIn>",self.limpiarTextos)
        self.entrada_usuario.grid(row=self.cantidad_campos + 2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

        self.boton_aceptar = tk.Button(self, text="enviar", command=self.Opciones)
        self.boton_aceptar.grid(row=self.cantidad_campos + 2, column=6, columnspan=6, padx=10, pady=10, sticky="w")

#-----------------------------------------------------------------------------------------

    def limpiarTextos(self, event):
        
        if self.entrada_usuario.get() == "Ingrese un numero":
            self.entrada_usuario.delete(0, tk.END)  

#-----------------------------------------------------------------------------------------
    #Primera opcion
    
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
        boton_regresar = tk.Button(self, text="Regresar",bg="#3BA8F9",command=self.volver_principal)
        boton_regresar.grid(row=8, column=3, padx=5, pady=5, sticky="w")

#-----------------------------------------------------------------------------------------
    
    #Segunda opcion
    
    def interfaz_2(self,label_1):
        for idx, texto in enumerate(label_1):
            fila = idx % 9  
            columna = idx // 9  

            lab = tk.Label(self, text=texto, borderwidth=1, relief="solid")
            lab.grid(row=fila, column=columna, padx=5, pady=5, sticky="w")
        
        boton_regresar = tk.Button(self, text="Seguir",bg="#3BA8F9",command=lambda: self.interfaz_2_1())
        boton_regresar.grid(row=8, column=3, padx=5, pady=5, sticky="w")
    

    def interfaz_2_1 (self):
        for widget in self.winfo_children():
                widget.destroy()
        label_producto = tk.Label(self, text="Elija el producto que desea comprar", justify="center")
        label_producto.grid(row=0, column=0)

        entry_producto = tk.Entry(self, width=30, justify='center')
        entry_producto.grid(row=0, column=1)

        label_unidades = tk.Label(self, text="¿Cuántas unidades desea comprar?", justify="center")
        label_unidades.grid(row=1, column=0)

        entry_unidades = tk.Entry(self, width=30, justify='center')
        entry_unidades.grid(row=1, column=1)

        boton_seguir = tk.Button(self, text="seguir",bg="#3BA8F9",command=lambda: self.interfaz_2_2(entry_producto.get(),entry_unidades.get()))
        boton_seguir.grid(row=8, column=3, padx=5, pady=5, sticky="w")


    def interfaz_2_2 (self,producto,cantidad):
        for widget in self.winfo_children():
                widget.destroy()
        int_producto = int(producto)
        int_cantidad = int(cantidad)
        #-----------------------------------------------------------------
        def validar_entrada():
            try:
                if (int_producto < 1) or (int_producto > 35):
                    raise ValueError("El número debe estar entre 1 y 35")       #Bloque de excepcion de numero          
            except ValueError:
                if producto.isdigit():
                    messagebox.showinfo("Cuidado!","Ingrese un número válido entre 1 y 35")            
                    return False
                if producto == "":
                    messagebox.showinfo("Cuidado!","Ingrese un número válido")
                    return False
                else:
                    messagebox.showinfo("Cuidado!","Ingrese un número válido (no letras)")
                    return False
            return True
        if not validar_entrada():
            return self.interfaz_2_1()
        #-----------------------------------------------------------------
        puaux = []
        contador = 0
        for ven in UsuarioRepositorio.obtener():
            for pu in ven.getPublicaciones():
                if (pu.getProducto().getNombre() == Producto.getProductos()[select].getNombre() and
                        pu.getInventario() > cantidad):
                    print(f"{contador + 1}. {pu.mostrarPublicacion()}")
                    puaux.append(pu)
                    contador += 1
        #-----------------------------------------------------------------
        def validar_entrada_1():
            try:
                if len(puaux) <= 0:
                    raise ValueError("No existen publicaciones de este producto o que tenga las unidades requeridas, regresando al menú")
            except ValueError:
                if len(puaux) <= 0:
                    messagebox.showinfo("No existen publicaciones de este producto o que tenga las unidades requeridas, regresando al menú")            
        if not validar_entrada_1():
            return self.interfaz_2_1()
        #Comprobar y sacar excepcion por el indice de lista y cantidad disponible
        #Hacer excepcion si paux no contiene elementos
        #Mostrar las publicaciones y hacer la revision de que el indice no se pase de las disponibles en la lista paux
        #compra = ProductoTransaccion(puaux[select1 - 1], cantidad_deseada)
        #carrito.agregarProducto(compra)
        boton_seguir = tk.Button(self, text="seguir",bg="#3BA8F9",command=self.confirmacion_1)
        boton_seguir.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    def confirmacion_1 (self):
        for widget in self.winfo_children():
                widget.destroy()
        confirmacion_label = tk.Label(self, text="Producto agregado correctamente al carrito")
        confirmacion_label.grid(row=0, column=0, padx=5, pady=5)

        boton_regresar = tk.Button(self, text="Regresar",bg="#3BA8F9",command=self.volver_principal)
        boton_regresar.grid(row=1, column=0)


#-----------------------------------------------------------------------------------------

    #Tercera opcion

    def interfaz_3(self):
        
        label_eliminar = tk.Label(self, text="Elija el producto que desea eliminar del carrito", justify="center", bd=2, relief="solid")
        label_eliminar.grid(row=0, column=0,padx=5,sticky="w")

        entry_eliminar = tk.Entry(self, width=20, justify='center')
        entry_eliminar.grid(row=0, column=3)

        label_eliminar = tk.Label(self, text="Cuantas unidades desea eliminar", justify="center", bd=2, relief="solid")
        label_eliminar.grid(row=1, column=0,padx=5,pady=10,sticky="w")

        entry_eliminar = tk.Entry(self, width=20, justify='center')
        entry_eliminar.grid(row=1, column=3,pady=10)

        boton_eliminar = tk.Button(self, text="Seguir", bg="#3BA8F9", command=self.interfaz_3_1)
        boton_eliminar.grid(row=2, columnspan=2,pady=10,sticky="e")
    
    def interfaz_3_1(self):
        for widget in self.winfo_children():
            widget.destroy()
        #Organizar excepcion por si alguno de los labels esta vacio o se le dan letras numeros fuera de rango
        boton_eliminar = tk.Button(self, text="Confirmar", bg="#3BA8F9", command=self.interfaz_3_2)
        boton_eliminar.grid(row=2, columnspan=2,pady=10,sticky="e")
    
    def interfaz_3_2(self):
        for widget in self.winfo_children():
                widget.destroy()
        confirmacion_label = tk.Label(self, text="Producto eliminado correctamente del carrito")
        confirmacion_label.grid(row=0, column=0, padx=5, pady=5)

        boton_regresar = tk.Button(self, text="Regresar",bg="#3BA8F9",command=self.volver_principal)
        boton_regresar.grid(row=1, column=0)

#-----------------------------------------------------------------------------------------

    def interfaz_5(self):
        label = tk.Label(self, text="¿Qué desea modificar?", bd=2, relief="solid",bg="#BAD526")
        label.grid(row=0, column=0, columnspan=3, pady=10,padx=10)

        boton_opcion_1 = tk.Button(self, text="Modificar cantidad de un producto", command=self.modificar)
        boton_opcion_1.grid(row=1, column=0, pady=10,padx=10)

        boton_opcion_2 = tk.Button(self, text="Vaciar carrito completamente", command=self.vaciar_carrito)
        boton_opcion_2.grid(row=2, column=0, pady=10,padx=10)

        boton_opcion_3 = tk.Button(self, text="Volver al menú principal", command=self.volver_principal)
        boton_opcion_3.grid(row=3, column=0, pady=10,padx=10)
    
    def modificar(self):
        #Mostrar el carrito, mediante la implementación y las excepciones si no selecciona un producto disponible
        boton_eliminar = tk.Button(self, text="Seguir", bg="#3BA8F9", command=self.modificar_1)
        boton_eliminar.grid(row=2, columnspan=2,pady=10,sticky="e")
    
    def modificar_1(self):
        pass

    def vaciar_carrito(self):
        pass


#-----------------------------------------------------------------------------------------

    def Opciones(self):
        elegido = self.entrada_usuario.get()
        def validar_entrada():
            try:
                opcion = int(elegido)
                if (opcion < 1) or (opcion > 11):
                    raise ValueError("El número debe estar entre 1 y 11")        #Bloque de excepcion de numero          
            except ValueError:
                if elegido.isdigit():
                    messagebox.showinfo("Cuidado!","Ingrese un número válido entre 1 y 11")            
                    return False
                if elegido == "":
                    messagebox.showinfo("Cuidado!","Ingrese un número válido")
                    return False
                else:
                    messagebox.showinfo("Cuidado!","Ingrese un número válido (no letras)")
                    return False
            return True
        if not validar_entrada():
            return                                                          
        #---------------------------------------------------------------
        if elegido == "1":
            for widget in self.winfo_children():
                widget.destroy()
            pro = []
            num = 1
            for i in ProductoRepositorio.get_productos():
                pro.append(f"{num}. {i.getNombre()}")
                num = num + 1
            self.interfaz_1(pro)

        if elegido == "2":
            for widget in self.winfo_children():
                widget.destroy()
            pro = []
            num = 1
            for i in ProductoRepositorio.get_productos():
                pro.append(f"{num}. {i.getNombre()}")
                num = num + 1
            self.interfaz_2(pro)

        if elegido == "3":
            for widget in self.winfo_children():
                widget.destroy()
            self.interfaz_3()
        
        if elegido == "5":
            for widget in self.winfo_children():
                widget.destroy()
            self.interfaz_5()