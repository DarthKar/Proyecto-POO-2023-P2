import tkinter as tk
from tkinter import font

# Crear una ventana principal
root = tk.Tk()

# Obtener la lista de fuentes disponibles
fuentes_disponibles = font.families()

# Imprimir la lista de fuentes
print(fuentes_disponibles)

# Puedes cerrar la ventana después de obtener la lista si no la necesitas
root.destroy()
