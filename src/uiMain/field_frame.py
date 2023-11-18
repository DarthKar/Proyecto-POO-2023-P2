import tkinter as tk
from tkinter import messagebox

class FieldFrame(tk.Frame):
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
            self.habilitado = [True] * self.cantidad_campos

        if self.valores is None:
            self.valores = [""] * self.cantidad_campos

        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio, font=("Arial", 10))
        label_titulo_criterio.grid(row=0, column=0, columnspan=6, sticky="w")

        label_titulo_valores = tk.Label(self, text=self.tituloValores, font=("Arial", 10))
        label_titulo_valores.grid(row=0, column=6, columnspan=6, sticky="w")

        for i in range(self.cantidad_campos):
            label_criterio = tk.Label(self, text=f"{self.nombres_criterios[i]}")
            label_criterio.grid(row=i + 1, column=0, columnspan=6, sticky="w")

            entry = tk.Entry(self, state='normal' if self.habilitado[i] else 'disabled')
            entry.insert(0, self.valores[i])
            entry.grid(row=i + 1, column=6, columnspan=6, sticky="w")
        
        self.boton_aceptar = tk.Button(self, text="Aceptar", command=self.guardarValores)
        self.boton_aceptar.grid(row=self.cantidad_campos + 2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

        self.boton_clear = tk.Button(self, text="Limpiar", command=self.limpiarTextos)
        self.boton_clear.grid(row=self.cantidad_campos + 2, column=6, columnspan=6, padx=10, pady=10, sticky="w")

    def guardarValores(self):
        self.Valores = []
        for i in range(self.cantidad_campos):
            valor = self.getValue(i)
            self.Valores.append(valor)
        self.pulsado = True
        self.limpiarTextos()
        print(self.Valores)
        return self.Valores

    def getValue(self, index):
        entry_widget = self.grid_slaves(row=index + 1, column=6)[0]
        return entry_widget.get()

    def limpiarTextos(self):
        for entry_widget in self.grid_slaves(column=6):
            if isinstance(entry_widget, tk.Entry):
                entry_widget.delete(0, tk.END)
