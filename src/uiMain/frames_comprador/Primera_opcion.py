import tkinter as tk
from tkinter import messagebox

class Primera_opcion(tk.Frame):
    def __init__(self, master, tituloCriterio, nombres_criterios, cantidad_campos):
        super().__init__(master, width=500, height=500)
        self.tituloCriterio = tituloCriterio
        self.cantidad_campos = cantidad_campos
        self.nombres_criterios = nombres_criterios
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
