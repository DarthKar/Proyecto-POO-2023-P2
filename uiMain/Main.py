import tkinter as tk

def CV():
    actual = listaCv.index(label_p2.cget("text"))
    cambio = (actual + 1) % len(listaCv)
    label_p2.config(text=listaCv[cambio])
    label_p2_fotos.config(image=imgCv[cambio])

ventana = tk.Tk()
ventana.title("Choope")
ventana.geometry("600x500")

# Fotos y textos de CV
fotoCv1 = tk.PhotoImage(file="src/image1.gif")
imgCv = [fotoCv1]

listaCv = [
    "Miguel Angel Peña, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)


ventanaInicio = tk.Frame(ventana)
ventanaInicio.pack(fill="both", expand=True)

menuInicio = tk.Menu(ventana)
ventana.config(menu=menuInicio)

menu1 = tk.Menu(menuInicio, font=("italic", 16))
menuInicio.add_cascade(label="Inicio", menu=menu1)
menuInicio.add_command(label="Salir")

framePrincipal = tk.Frame(ventanaInicio, bg="red")
framePrincipal.pack(fill="both", expand=True, padx=10)

p1 = tk.Frame(framePrincipal, bg="blue")
p1.pack(side="left", padx=10, fill="both", expand=True)

p2 = tk.Frame(framePrincipal, bg="black")
p2.pack(side="right", padx=10, fill="both", expand=True)

label_p2 = tk.Label(p2, text=listaCv[0], font=("italic", 15), wraplength=270)
label_p2.grid(row=0, column=0, pady=10, padx=10)
label_p2.bind("<Button-1>", lambda event: CV())
label_p2_fotos = tk.Label(p2, image=imgCv[0])
label_p2_fotos.grid(row=4, column=0, pady=10, padx=10)

p3 = tk.Frame(p1, bg="green")
p3.pack(side="top", padx=10, pady=10, fill="both", expand=True)
label_p3 = tk.Label(p3, text="¡Bienvenido a Choope!", font=("italic", 16))
label_p3.pack(pady=10)

p4 = tk.Frame(p1, bg="green")
p4.pack(padx=10, pady=10, fill="both", expand=True)
label_foto1 = tk.Label(p4)
foto1 = tk.PhotoImage(file="src/image1.gif")
label_foto1.config(image=foto1, compound="bottom")
label_foto1.pack(pady=10, padx=10)
botonVentanaUsuario = tk.Button(p4, text="Usuario interfaz", padx=10, pady=10)
botonVentanaUsuario.pack()

ventana.mainloop()
