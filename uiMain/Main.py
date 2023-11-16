import tkinter as tk
from PIL import Image, ImageTk

def CV():
    actual = listaCv.index(label_p2.cget("text"))
    cambio = (actual + 1) % len(listaCv)
    label_p2.config(text=listaCv[cambio])

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
        LabelDesc.config(text= "Realizar Devolución")
        LabelDesc2.config(text="Aquí va la descripción para realizar una devolución.")
  
    elif proceso == "Opinion":
        LabelDesc.config(text="Opinar")
        LabelDesc2.config(text="Aquí va la descripción para dejar una opinión.")

    elif proceso == "Estadistica":
        LabelDesc.config(text="Estadística")
        LabelDesc2.config(text=" Aquí va la descripción para ver estadísticas.")
  

ventana = tk.Tk()
ventana.title("Choopi")
ventana.geometry("600x500")



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

menu1 = tk.Menu(menuInicio, font=("italic"), tearoff=0)
menuInicio.add_cascade(label="Inicio", menu=menu1)
menu1.add_command(label="Descripcion")
menu1.add_separator()
menu1.add_command(label="Salir", command=quit)

framePrincipal = tk.Frame(ventanaInicio, bg="red")
framePrincipal.pack(fill="both", expand=True, padx=10)

p1 = tk.Frame(framePrincipal, bg="blue")
p1.pack(side="left", padx=10, fill="both", expand=True)

p2 = tk.Frame(framePrincipal, bg="black")
p2.pack(side="right", padx=10, fill="both", expand=True)

p2_label_frame = tk.Frame(p2, bg="white")
p2_label_frame.pack(pady=10)
label_p2 = tk.Label(p2_label_frame, text=listaCv[0], font=("italic", 15), wraplength=270)
label_p2.grid(row=0, column=0,columnspan=2)
label_p2.bind("<Button-1>", lambda event: CV())
p2_fotos_frame = tk.Frame(p2, bg="white")
p2_fotos_frame.pack(pady=10)

image_path = "src\MiguelImage.jpg"
pil=Image.open(image_path)

img = ImageTk.PhotoImage(file=image_path)

# Cambia esta línea para usar label_p2_fotos en lugar de labelFotoCV
label_p2_fotos = tk.Label(p2_fotos_frame, image=img)
label_p2_fotos.grid(row=4, column=0)

p3 = tk.Frame(p1, bg="green")
p3.pack(side="top", padx=10, pady=10, fill="both", expand=True)
label_p3 = tk.Label(p3, text="¡Bienvenido a Choopi!", font=("italic",20))
label_p3.pack(pady=10)

p4 = tk.Frame(p1, bg="green")
p4.pack(padx=10, pady=10, fill="both", expand=True)
label_foto1 = tk.Label(p4)
foto1 = tk.PhotoImage(file="src/image1.gif")
label_foto1.config(image=foto1, compound="bottom")
label_foto1.pack(pady=10, padx=10)
botonVentanaUsuario = tk.Button(p4, text="Usuario interfaz", padx=10, pady=10, command=cambioDeVentana)
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

MenuFuncionalidades= tk.Menu(menuP, font=("italic"), tearoff=0)
menuP.add_cascade(label="Procesos y consultas", menu=MenuFuncionalidades)
MenuFuncionalidades.add_command(label="Realizar Compra", command=lambda: cambiarContenido("Compra"))
MenuFuncionalidades.add_command(label="Realizar Devolucion", command=lambda: cambiarContenido("Devolucion"))
MenuFuncionalidades.add_command(label="Opinar", command=lambda: cambiarContenido("Opinion"))
MenuFuncionalidades.add_command(label="Estadistica", command=lambda: cambiarContenido("Estadistica"))

frameContenedor=tk.Frame(ventanaPrincipalI, bg="blue")
frameContenedor.pack(fill="both", expand=True)

frameDelLabelDesc=tk.Frame(frameContenedor)
frameDelLabelDesc.pack(pady=10)
LabelDesc=tk.Label(frameDelLabelDesc,text="NOMBRE PROCESO",bg="white", font=("italic", 15), wraplength=270)
LabelDesc.grid(row=0, column=0, columnspan=2)

frameDelLabelDesc2=tk.Frame(frameContenedor)
frameDelLabelDesc2.pack(pady=10)
LabelDesc2 = tk.Label(frameDelLabelDesc2,text="DESCRIPCION PROCESO O FUNCIONALIDAD", font=("italic", 15), wraplength=400)
LabelDesc2.grid(row=2, column=0,columnspan=4)

FrameWidgets=tk.Frame(frameContenedor, bg="white")
FrameWidgets.pack(pady=10)


ventanaPrincipalI.withdraw()

ventana.mainloop()
