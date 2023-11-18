import tkinter as tk

def actualizar_texto():
    texto = entrada_texto.get("1.0", "end-1c")
    etiqueta.config(text=texto)

ventana = tk.Tk()
ventana.title("Ejemplo de Texto con Ajuste y Saltos de Línea")

# Entrada de texto
entrada_texto = tk.Text(ventana, wrap="word", width=30, height=10)
entrada_texto.pack(pady=10)

# Botón para actualizar el texto
boton_actualizar = tk.Button(ventana, text="Actualizar Texto", command=actualizar_texto)
boton_actualizar.pack(pady=5)

# Etiqueta que mostrará el texto ajustado
etiqueta = tk.Label(ventana, text="", wraplength=200)
etiqueta.pack(pady=10)

ventana.mainloop()
