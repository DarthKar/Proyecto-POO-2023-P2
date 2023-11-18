import tkinter as tk
from PIL import Image, ImageTk


def CV():
    actual = listaCv.index(label_p2.cget("text"))
    cambio = (actual + 1) % len(listaCv)
    label_p2.config(text=listaCv[cambio])
    label_p2.config(bg="gray")
    label_p2_fotos.config(image=listaImagenesCv[cambio])


def cambioDeVentana():
    ventana.withdraw()
    ventanaPrincipalI.deiconify()


def volverVentana():
    ventanaPrincipalI.withdraw()
    ventana.deiconify()


def cambiarContenido(proceso):
    # Lógica para cambiar el contenido según el proceso seleccionado
    if proceso == "Compra":
        LabelDesc.config(text="Realizar Compra")
        LabelDesc2.config(text="Aquí va la descripción para realizar una compra.")
    

    elif proceso == "Devolucion":
        LabelDesc.config(text="Realizar Devolución")
        LabelDesc2.config(text="Aquí va la descripción para realizar una devolución.")

    elif proceso == "opinion":
        LabelDesc.config(text="Opinar")
        LabelDesc2.config(text="Aquí va la descripción para dejar una opinión.")
        opinion()
        

    elif proceso == "Estadistica":
        LabelDesc.config(text="Estadística")
        LabelDesc2.config(text=" Aquí va la descripción para ver estadísticas.")

def cargar_imagenes():
    tempList = []
    for i in range(0, len(listaCv)):
        tempList.append(ImageTk.PhotoImage(Image.open(f"src/{i + 1}.gif").resize((200,356))))
    return tempList


def opinion():
    
    for widget in FrameWidgets.winfo_children():
        widget.destroy()
    label_entry1 = tk.Label(FrameWidgets, text="Nombre:", font=("italic", 12), padx=5, pady=5)
    label_entry1.grid(row=0, column=0, sticky="e")

    entry1 = tk.Entry(FrameWidgets, font=("italic", 12), width=30)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    label_entry2 = tk.Label(FrameWidgets, text="Comentario:", font=("italic", 12), padx=5, pady=5)
    label_entry2.grid(row=1, column=0, sticky="e")

    entry2 = tk.Entry(FrameWidgets, font=("italic", 12), width=30)
    entry2.grid(row=1, column=1, padx=5, pady=5)



ventana = tk.Tk()
ventana.config(bg="black")
ventana.title("Choopi")
ventana.geometry("600x500")

listaCv = [
    "Miguel Angel Peña, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
    "Juan Pablo Gaviria Orozco, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
    "Sebastian Gomez Zapata, 22 años, estudiante de la Universidad Nacional de Colombia sede Medellin de Ingenieria de Sistemas",
    "Juan Felipe Cadavid Ruiz, estudaitne de Ingenieria de Sistemas e Informatica, Universidad Nacional de Colombia"
]

listaImagenesCv = cargar_imagenes()

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

ventanaInicio = tk.Frame(ventana)
ventanaInicio.pack(fill="both", expand=True)

menuInicio = tk.Menu(ventana)
ventana.config(menu=menuInicio)

#Creacion Menu Inicio
menu1 = tk.Menu(menuInicio, font=("italic"), tearoff=0)
menuInicio.add_cascade(label="Inicio", menu=menu1)
menu1.add_command(label="Descripcion")
menu1.add_separator()
menu1.add_command(label="Salir", command=quit)

framePrincipal = tk.Frame(ventanaInicio, bg="black")
framePrincipal.pack(fill="both", expand=True, padx=10)

p1 = tk.Frame(framePrincipal, bg="dark blue")
p1.pack(side="left", padx=10, fill="both", expand=True)

p2 = tk.Frame(framePrincipal, bg="black")
p2.pack(side="right", padx=10, fill="both", expand=True)

#Creacion Frame CV
p2_label_frame = tk.Frame(p2, bg="white")
p2_label_frame.pack(side="top", fill="both", expand=True)
label_p2 = tk.Label(p2_label_frame, text=listaCv[0], font=("italic", 15), wraplength=270)
label_p2.pack(pady=10)
label_p2.bind("<Button-1>", lambda event: CV())
p2_fotos_frame = tk.Frame(p2, bg="white")
p2_fotos_frame.pack(pady=10)

img = Image.open("src/1.gif")
resized_img = img.resize((125, 150))

pil = ImageTk.PhotoImage(resized_img)

img2 = Image.open("src/2.gif")

pil2 = ImageTk.PhotoImage(img2)
img3 = Image.open("src/3.gif")

pil3 = ImageTk.PhotoImage(img3)
img4 = Image.open("src/4.gif")

pil4 = ImageTk.PhotoImage(img4)

label_p2_fotos = tk.Label(p2_fotos_frame, image=pil, )
label_p2_fotos.grid(row=4, column=0, pady=5, padx=5, sticky="news")
label_p3_fotos = tk.Label(p2_fotos_frame, image=pil, )
label_p3_fotos.grid(row=3, column=0, pady=5, padx=5, sticky="news")
label_p4_fotos = tk.Label(p2_fotos_frame, image=pil, )
label_p4_fotos.grid(row=4, column=1, pady=5, padx=5, sticky="news")
label_p5_fotos = tk.Label(p2_fotos_frame, image=pil, )
label_p5_fotos.grid(row=3, column=1, pady=5, padx=5, sticky="news")

#Frame Bienvenida
p3 = tk.Frame(p1, bg="light blue")
p3.pack(side="top", padx=10, pady=10, fill="both", expand=True)
label_p3 = tk.Label(p3, text="¡Bienvenido a Choopi!", font=("italic", 20))
label_p3.pack(pady=10)

p4 = tk.Frame(p1, bg="light blue")
p4.pack(padx=10, pady=10, fill="both", expand=True)
label_foto1 = tk.Label(p4)
foto1 = tk.PhotoImage(file="src/2.gif")
label_foto1.config(image=foto1, compound="bottom")
label_foto1.pack(pady=10, padx=10)
botonVentanaUsuario = tk.Button(p4, text="usuario interfaz", padx=10, pady=10, command=cambioDeVentana)
botonVentanaUsuario.pack()

ventanaPrincipalI = tk.Toplevel()
ventanaPrincipalI.title("choopi")
ventanaPrincipalI.geometry("600x500")

menuP = tk.Menu(ventanaPrincipalI, tearoff=0)
ventanaPrincipalI.config(menu=menuP)

menuArchivo = tk.Menu(menuP, font=("italic"), tearoff=0)
menuP.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.add_command(label="Aplicacion")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=volverVentana)

MenuFuncionalidades = tk.Menu(menuP, font=("italic"), tearoff=0)
menuP.add_cascade(label="Procesos y consultas", menu=MenuFuncionalidades)
MenuFuncionalidades.add_command(label="Realizar Compra", command=lambda: cambiarContenido("Compra"))
MenuFuncionalidades.add_command(label="Realizar Devolucion", command=lambda: cambiarContenido("Devolucion"))
MenuFuncionalidades.add_command(label="Opinar", command=lambda: cambiarContenido("opinion"))
MenuFuncionalidades.add_command(label="Estadistica", command=lambda: cambiarContenido("Estadistica"))

frameContenedor = tk.Frame(ventanaPrincipalI, bg="blue")
frameContenedor.pack(fill="both", expand=True)

frameDelLabelDesc = tk.Frame(frameContenedor)
frameDelLabelDesc.pack(pady=10)
LabelDesc = tk.Label(frameDelLabelDesc, text="a", bg="white", font=("italic", 15), wraplength=270)
LabelDesc.grid(row=0, column=0, columnspan=2)

frameDelLabelDesc2 = tk.Frame(frameContenedor)
frameDelLabelDesc2.pack(pady=10)
LabelDesc2 = tk.Label(frameDelLabelDesc2, text="DESCRIPCION PROCESO O FUNCIONALIDAD", font=("italic", 15),
                      wraplength=400)
LabelDesc2.grid(row=2, column=0, columnspan=4)

FrameWidgets = tk.Frame(frameContenedor, bg="white")
FrameWidgets.pack(pady=10)
cambiarContenido("Compra")


ventanaPrincipalI.withdraw()

ventana.mainloop()
