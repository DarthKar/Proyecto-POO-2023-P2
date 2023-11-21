import tkinter as tk
from tkinter import messagebox
from src.uiMain.field_frame import FieldFrame


class opinion_principal(FieldFrame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores=None, habilitado=None):
        super().__init__(master,tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores, habilitado)
        for widget in self.winfo_children():
            widget.destroy()
        
   
   
#----------------------------------------------------------------------------------------
    def Opciones(self):
            elegido = self.entrada_usuario.get()
            def validar_entrada():
                try:
                    opcion = int(elegido)
                    if (opcion < 1) or (opcion > 6):
                        raise ValueError("El número debe estar entre 1 y 6")        #Bloque de excepcion de numero          
                except ValueError:
                    if elegido.isdigit():
                        messagebox.showinfo("Cuidado!","Ingrese un número válido entre 1 y 6")            
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

            entry_valor = tk.StringVar()
            entry_valor.set("Escriba aqui")
            entry_valor1 = tk.StringVar()
            entry_valor1.set("Escriba aqui")
            entry_valor2 = tk.StringVar()
            entry_valor2.set("Escriba aqui")
            entry_valor3 = tk.StringVar()
            entry_valor3.set("Escriba aqui")
                
            def generarBotones():
                  
                botonAceptar = tk.Button(self,text="Aceptar", bg="#35B907", command=self.volver_principal)
                botonAceptar.grid(row=4, column=5, columnspan=2, sticky="w", pady=10, padx=10)
                
                botonSalir = tk.Button(self,text="Salir", bg="#FE1700", command=self.volver_principal)
                botonSalir.grid(row=4, column=0, columnspan=2, sticky="w", pady=10, padx=10)

                botonLimpiar = tk.Button(self,text="Limpiar", bg="#BFEC27", command=self.volver_principal)
                botonLimpiar.grid(row=4, column=3, columnspan=2, sticky="w", pady=10, padx=10)

            if elegido == "1":
                for widget in self.winfo_children():
                    widget.destroy()
                

                numeroDeIdentificacion = tk.Label(self, text="Identificacion", font=("YU Gothic", 10))
                numeroDeIdentificacion.grid(row=0,column=0,columnspan=6, sticky="w", padx=10,pady=10)
                
                entryIdent = tk.Entry(self, state="normal",textvariable=entry_valor,justify='center')
                entryIdent.bind("<FocusIn>",self.limpiarTextos)
                entryIdent.grid(row=0, column=6, columnspan=6, sticky="w",padx=10,pady=10)

                labeldeid = tk.Label(self, text="Id del producto", font=("YU Gothic", 10))
                labeldeid.grid(row=1, column=0, columnspan=6, sticky="w", padx=10,pady=10)
              
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor1,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=1, column=6, columnspan=6, sticky="w", padx=10,pady=10)

                labeldeCO = tk.Label(self, text="Comentario", font=("YU Gothic", 10))
                labeldeCO.grid(row=2, column=0, columnspan=6, sticky="w", pady=10, padx=10)
              
                entryCO = tk.Entry(self, state="normal",textvariable=entry_valor2,justify='center')
                entryCO.bind("<FocusIn>",self.limpiarTextos)
                entryCO.grid(row=2, column=6, columnspan=6, sticky="w",pady=10, padx=10)

                labeldeVA = tk.Label(self, text="Valoracion", font=("YU Gothicb", 10))      
                labeldeVA.grid(row=3, column=0, columnspan=6, sticky="w", pady=10,padx=10)
               
                entryVa = tk.Entry(self, state="normal",textvariable=entry_valor3,justify='center')
                entryVa.bind("<FocusIn>",self.limpiarTextos)
                entryVa.grid(row=3, column=6, columnspan=6, sticky="w", pady=10, padx=10)

                generarBotones()


            if elegido == "2":
                for widget in self.winfo_children():
                    widget.destroy()
                

                numeroDeIdentificacion = tk.Label(self, text="Identificacion", font=("YU Gothic", 10))
                numeroDeIdentificacion.grid(row=0,column=0,columnspan=6, sticky="w", padx=10,pady=10)
                
                entryIdent = tk.Entry(self, state="normal",textvariable=entry_valor,justify='center')
                entryIdent.bind("<FocusIn>",self.limpiarTextos)
                entryIdent.grid(row=0, column=6, columnspan=6, sticky="w",padx=10,pady=10)

                labeldeid = tk.Label(self, text="Id del producto", font=("YU Gothic", 10))
                labeldeid.grid(row=1, column=0, columnspan=6, sticky="w", padx=10,pady=10)
              
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor1,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=1, column=6, columnspan=6, sticky="w", padx=10,pady=10)

                labeldeCO = tk.Label(self, text="Comentario", font=("YU Gothic", 10))
                labeldeCO.grid(row=2, column=0, columnspan=6, sticky="w", pady=10, padx=10)
              
                entryCO = tk.Entry(self, state="normal",textvariable=entry_valor2,justify='center')
                entryCO.bind("<FocusIn>",self.limpiarTextos)
                entryCO.grid(row=2, column=6, columnspan=6, sticky="w",pady=10, padx=10)

                labeldeVA = tk.Label(self, text="Valoracion", font=("YU Gothicb", 10))      
                labeldeVA.grid(row=3, column=0, columnspan=6, sticky="w", pady=10,padx=10)
               
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor3,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=3, column=6, columnspan=6, sticky="w", pady=10, padx=10)

                generarBotones()

            if elegido == "3":
                for widget in self.winfo_children():
                        widget.destroy()
                

                numeroDeIdentificacion = tk.Label(self, text="Identificacion", font=("YU Gothic", 10))
                numeroDeIdentificacion.grid(row=0,column=0,columnspan=6, sticky="w", padx=10,pady=10)

                entryIdent = tk.Entry(self, state="normal",textvariable=entry_valor,justify='center')
                entryIdent.bind("<FocusIn>",self.limpiarTextos)
                entryIdent.grid(row=0, column=6, columnspan=6, sticky="w",padx=10,pady=10)

                labeldeid = tk.Label(self, text="Id del producto", font=("YU Gothic", 10))
                labeldeid.grid(row=1, column=0, columnspan=6, sticky="w", padx=10,pady=10)
              
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor1,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=1, column=6, columnspan=6, sticky="w", padx=10,pady=10)

                generarBotones()


            if elegido == "4":
                for widget in self.winfo_children():
                    widget.destroy()
                

                numeroDeIdentificacion = tk.Label(self, text="Identificacion", font=("YU Gothic", 10))
                numeroDeIdentificacion.grid(row=0,column=0,columnspan=6, sticky="w", padx=10,pady=10)
                
                entryIdent = tk.Entry(self, state="normal",textvariable=entry_valor,justify='center')
                entryIdent.bind("<FocusIn>",self.limpiarTextos)
                entryIdent.grid(row=0, column=6, columnspan=6, sticky="w",padx=10,pady=10)

                labeldeid = tk.Label(self, text="Id del vendedor", font=("YU Gothic", 10))
                labeldeid.grid(row=1, column=0, columnspan=6, sticky="w", padx=10,pady=10)
              
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor1,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=1, column=6, columnspan=6, sticky="w", padx=10,pady=10)

                labeldeCO = tk.Label(self, text="Comentario", font=("YU Gothic", 10))
                labeldeCO.grid(row=2, column=0, columnspan=6, sticky="w", pady=10, padx=10)
              
                entryCO = tk.Entry(self, state="normal",textvariable=entry_valor2,justify='center')
                entryCO.bind("<FocusIn>",self.limpiarTextos)
                entryCO.grid(row=2, column=6, columnspan=6, sticky="w",pady=10, padx=10)

                labeldeVA = tk.Label(self, text="Valoracion", font=("YU Gothicb", 10))      
                labeldeVA.grid(row=3, column=0, columnspan=6, sticky="w", pady=10,padx=10)
               
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor3,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=3, column=6, columnspan=6, sticky="w", pady=10, padx=10)
                
                generarBotones()

            if elegido == "5":
                for widget in self.winfo_children():
                    widget.destroy()
                

                numeroDeIdentificacion = tk.Label(self, text="Identificacion", font=("YU Gothic", 10))
                numeroDeIdentificacion.grid(row=0,column=0,columnspan=6, sticky="w", padx=10,pady=10)
                
                entryIdent = tk.Entry(self, state="normal",textvariable=entry_valor,justify='center')
                entryIdent.bind("<FocusIn>",self.limpiarTextos)
                entryIdent.grid(row=0, column=6, columnspan=6, sticky="w",padx=10,pady=10)

                labeldeid = tk.Label(self, text="Id del vendedor", font=("YU Gothic", 10))
                labeldeid.grid(row=1, column=0, columnspan=6, sticky="w", padx=10,pady=10)
              
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor1,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=1, column=6, columnspan=6, sticky="w", padx=10,pady=10)

                labeldeCO = tk.Label(self, text="Comentario", font=("YU Gothic", 10))
                labeldeCO.grid(row=2, column=0, columnspan=6, sticky="w", pady=10, padx=10)
              
                entryCO = tk.Entry(self, state="normal",textvariable=entry_valor2,justify='center')
                entryCO.bind("<FocusIn>",self.limpiarTextos)
                entryCO.grid(row=2, column=6, columnspan=6, sticky="w",pady=10, padx=10)

                labeldeVA = tk.Label(self, text="Valoracion", font=("YU Gothicb", 10))      
                labeldeVA.grid(row=3, column=0, columnspan=6, sticky="w", pady=10,padx=10)
               
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor3,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=3, column=6, columnspan=6, sticky="w", pady=10, padx=10)

                generarBotones()

            if elegido == "6":
                for widget in self.winfo_children():
                        widget.destroy()
                

                numeroDeIdentificacion = tk.Label(self, text="Identificacion", font=("YU Gothic", 10))
                numeroDeIdentificacion.grid(row=0,column=0,columnspan=6, sticky="w", padx=10,pady=10)

                entryIdent = tk.Entry(self, state="normal",textvariable=entry_valor,justify='center')
                entryIdent.bind("<FocusIn>",self.limpiarTextos)
                entryIdent.grid(row=0, column=6, columnspan=6, sticky="w",padx=10,pady=10)

                labeldeid = tk.Label(self, text="Id del vendedor", font=("YU Gothic", 10))
                labeldeid.grid(row=1, column=0, columnspan=6, sticky="w", padx=10,pady=10)
              
                entryId = tk.Entry(self, state="normal",textvariable=entry_valor1,justify='center')
                entryId.bind("<FocusIn>",self.limpiarTextos)
                entryId.grid(row=1, column=6, columnspan=6, sticky="w", padx=10,pady=10)

                generarBotones()

            


    def limpiarTextos(self, event):
            entry = event.widget
            if entry.get() == "Escriba aqui":
                entry.delete(0, tk.END)



    def crearPrincipal(self):
        for widget in self.winfo_children():
                widget.destroy()
        if self.habilitado is None:
            self.habilitado = [False] * self.cantidad_campos

        if self.valores is None:
            self.valores = [""] * self.cantidad_campos

        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio, font=("YU Gothic", 10))
        label_titulo_criterio.grid(row=0, column=0, columnspan=6, sticky="w")

        label_titulo_valores = tk.Label(self, text=self.tituloValores, font=("YU Gothicb", 10))      #Interfaz principal
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
        self.entrada_usuario.insert(0,"Escriba aqui")
        self.entrada_usuario.bind("<FocusIn>",self.limpiarTextos)
        self.entrada_usuario.grid(row=self.cantidad_campos + 2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

        self.boton_aceptar = tk.Button(self, text="enviar", command=self.Opciones)
        self.boton_aceptar.grid(row=self.cantidad_campos + 2, column=6, columnspan=6, padx=10, pady=10, sticky="w")

#-----------------------------------------------------------------------------------------

    def volver_principal(self):
        for widget in self.winfo_children():
                widget.destroy()
        self.crearPrincipal()

   
#-----------------------------------------------------------------------------------------

    

     