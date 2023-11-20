import tkinter as tk
from tkinter import messagebox
from src.uiMain.field_frame import FieldFrame

class opinion_principal(FieldFrame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores=None, habilitado=None):
        super().__init__(master,tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores, habilitado)
        for widget in self.winfo_children():
            widget.destroy()
        

    def limpiarTextos(self, event):
        
        if self.entrada_usuario.get() == "Ingrese un numero":
            self.entrada_usuario.delete(0, tk.END)  


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
        FieldFrame(self,"Requerimientos",["Elija el producto que desea comprar","Cuantas unidades desea comprar"],2,"Introduce aqui los datos")
        boton_regresar = tk.Button(self, text="regresar",bg="#3BA8F9")
        boton_regresar.grid(row=8, column=3, padx=5, pady=5, sticky="w")


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
            pro = [
            "1.Camisa básica",
            "2.Pantalones vaqueros",
            "3.Zapatillas deportivas",
            "4.Mochila resistente",
            "5.Reloj elegante",
            "6.Gafas de sol polarizadas",
            "7.Auriculares inalámbricos",
            "8.Teclado mecánico",
            "9.Ratón ergonómico",
            "10.Cámara digital compacta",
            "11.Bicicleta de montaña",
            "12.Guantes de entrenamiento",
            "13.Gorra ajustable",
            "14.Bufanda de lana",
            "15.Manta suave de viaje",
            "16.Botella de agua deportiva",
            "17.Silla de oficina ergonómica",
            "18.Mesa plegable portátil",
            "19.Maletín ejecutivo",
            "20.Termo de acero inoxidable",
            "21.Lámpara LED de escritorio",
            "22.Juego de sartenes antiadherentes",
            "23.Cuaderno de notas premium",
            "24.Organizador de cables",
            "25.Máquina de café expresso",
            "26.Kit de herramientas domésticas",
            "27.Purificador de aire compacto",
            "28.Kit de pesas ajustables",
            "29.Caja de herramientas para bricolaje",
            "30.Abrelatas eléctrico",
            "31.Linterna recargable resistente al agua",
            "32.Aspiradora de mano",
            "33.Tostadora de pan automática",
            "34.Set de viaje para afeitado",
            "35.Bolsa térmica para picnic"
            ]
            self.interfaz_1(pro)

        if elegido == "2":
            pro = [
            "1.Camisa básica",
            "2.Pantalones vaqueros",
            "3.Zapatillas deportivas",
            "4.Mochila resistente",
            "5.Reloj elegante",
            "6.Gafas de sol polarizadas",
            "7.Auriculares inalámbricos",
            "8.Teclado mecánico",
            "9.Ratón ergonómico",
            "10.Cámara digital compacta",
            "11.Bicicleta de montaña",
            "12.Guantes de entrenamiento",
            "13.Gorra ajustable",
            "14.Bufanda de lana",
            "15.Manta suave de viaje",
            "16.Botella de agua deportiva",
            "17.Silla de oficina ergonómica",
            "18.Mesa plegable portátil",
            "19.Maletín ejecutivo",
            "20.Termo de acero inoxidable",
            "21.Lámpara LED de escritorio",
            "22.Juego de sartenes antiadherentes",
            "23.Cuaderno de notas premium",
            "24.Organizador de cables",
            "25.Máquina de café expresso",
            "26.Kit de herramientas domésticas",
            "27.Purificador de aire compacto",
            "28.Kit de pesas ajustables",
            "29.Caja de herramientas para bricolaje",
            "30.Abrelatas eléctrico",
            "31.Linterna recargable resistente al agua",
            "32.Aspiradora de mano",
            "33.Tostadora de pan automática",
            "34.Set de viaje para afeitado",
            "35.Bolsa térmica para picnic"
            ]
            for widget in self.winfo_children():
                widget.destroy()
            self.interfaz_2(pro)