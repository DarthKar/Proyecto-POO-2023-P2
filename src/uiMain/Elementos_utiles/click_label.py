import tkinter as tk

class LabelCambio(tk.Frame):
    def __init__(self, master, lista):
        super().__init__(master)

        self.lista = lista
        self.indice_actual = 0

        self.label = tk.Label(self, text=self.lista[self.indice_actual])
        self.label.pack()

        self.label.bind("<Button-1>", self.siguiente)
        self.label.bind("<Button-3>", self.anterior)

    def siguiente(self, event):
        self.indice_actual = (self.indice_actual + 1) % len(self.lista)
        self.label.config(text=self.lista[self.indice_actual])

    def anterior(self, event):
        self.indice_actual = (self.indice_actual - 1) % len(self.lista)
        self.label.config(text=self.lista[self.indice_actual])







