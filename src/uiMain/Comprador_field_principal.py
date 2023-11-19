import tkinter as tk
from tkinter import messagebox
from src.uiMain.frames_comprador.Primera_opcion import Primera_opcion


class Comprador_principal(tk.Frame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos, tituloValores, valores=None, habilitado=None):
        super().__init__(master, width=500, height=500)
        
        self.tituloCriterio = tituloCriterio
        self.cantidad_campos = cantidad_campos
        self.tituloValores = tituloValores
        self.nombres_criterios = nombres_criterios
        self.valores = valores
        self.habilitado = habilitado
        self.pulsado = False
        self.Valores = None
        self.pack()

        if self.habilitado is None:
            self.habilitado = [False] * self.cantidad_campos

        if self.valores is None:
            self.valores = [""] * self.cantidad_campos

        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio, font=("Arial", 10))
        label_titulo_criterio.grid(row=0, column=0, columnspan=6, sticky="w")

        label_titulo_valores = tk.Label(self, text=self.tituloValores, font=("Arial", 10))
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
        self.entrada_usuario.grid(row=self.cantidad_campos + 2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

        self.boton_aceptar = tk.Button(self, text="enviar", command=self.Opciones)
        self.boton_aceptar.grid(row=self.cantidad_campos + 2, column=6, columnspan=6, padx=10, pady=10, sticky="w")

    def Opciones(self):
        elegido = self.entrada_usuario.get()
        def validar_entrada():
            try:
                opcion = int(elegido)
                if (opcion < 1) or (opcion > 12):
                    raise ValueError("El número debe estar entre 1 y 12")        #Bloque de excepcion de numero          
            except ValueError:
                if elegido.isdigit():
                    messagebox.showinfo("Cuidado!","Ingrese un número válido entre 1 y 12")            
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
        

            