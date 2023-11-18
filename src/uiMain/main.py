import tkinter as tk
from PIL import Image, ImageTk

class Main:
    def CV(self):
        actual = self.listaCv.index(self.label_p2.cget("text"))
        cambio = (actual + 1) % len(self.listaCv)
        self.label_p2.config(text=self.listaCv[cambio])
        self.label_p2_fotos.config(image=self.listaImagenesCv[cambio])

    def cambioDeVentana(self):
        self.ventana.withdraw()
        self.ventanaPrincipalI.deiconify()

    def volverVentana(self):
        self.ventanaPrincipalI.withdraw()
        self.ventana.deiconify()

    def cambiarContenido(self, proceso):
        # Lógica para cambiar el contenido según el proceso seleccionado
        if proceso == "Compra":
            self.LabelDesc.config(text="Realizar Compra")
            self.LabelDesc2.config(text="Aquí va la descripción para realizar una compra.")
        elif proceso == "Devolucion":
            self.LabelDesc.config(text="Realizar Devolución")
            self.LabelDesc2.config(text="Aquí va la descripción para realizar una devolución.")
        elif proceso == "opinion":
            self.LabelDesc.config(text="Opinar")
            self.LabelDesc2.config(text="Aquí va la descripción para dejar una opinión.")
            self.opinion()
        
        elif proceso == "Estadistica":
            self.LabelDesc.config(text="Estadística")
            self.LabelDesc2.config(text=" Aquí va la descripción para ver estadísticas.")

    def cargar_imagenes(self):
        tempList = []
        for i in range(0, len(self.listaCv)):
            tempList.append(ImageTk.PhotoImage(Image.open(f"src/{i + 1}.gif").resize((200, 356))))
        return tempList

    def opinion(self):
        for widget in self.FrameWidgets.winfo_children():
            widget.destroy()
        label_entry1 = tk.Label(self.FrameWidgets, text="Nombre:", font=("italic", 12), padx=5, pady=5)
        label_entry1.grid(row=0, column=0, sticky="e")

        entry1 = tk.Entry(self.FrameWidgets, font=("italic", 12), width=30)
        entry1.grid(row=0, column=1, padx=5, pady=5)

        label_entry2 = tk.Label(self.FrameWidgets, text="Comentario:", font=("italic", 12), padx=5, pady=5)
        label_entry2.grid(row=1, column=0, sticky="e")

        entry2 = tk.Entry(self.FrameWidgets, font=("italic", 12), width=30)
        entry2.grid(row=1, column=1, padx=5, pady=5)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Choopi")
        self.ventana.geometry("600x500")

        self.listaCv = [
            "Miguel Angel Peña, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
            "Juan Pablo Gaviria Orozco, estudiante de Ingenieria en sistemas e informatica, Universidad Nacional De Colombia",
            "Sebastian Gomez Zapata, 22 años, estudiante de la Universidad Nacional de Colombia sede Medellin de Ingenieria de Sistemas",
            "Juan Felipe Cadavid Ruiz, estudaitne de Ingenieria de Sistemas e Informatica, Universidad Nacional de Colombia"
        ]

        self.listaImagenesCv = self.cargar_imagenes()

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(0, weight=1)

        self.ventanaInicio = tk.Frame(self.ventana)
        self.ventanaInicio.pack(fill="both", expand=True)

        self.menuInicio = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menuInicio)

        #Creacion Menu Inicio
        
        self.menu1 = tk.Menu(self.menuInicio, font=("italic"), tearoff=0)
        self.menuInicio.add_cascade(label="Inicio", menu=self.menu1)
        self.menu1.add_command(label="Descripcion")
        self.menu1.add_separator()
        self.menu1.add_command(label="Salir", command=quit)

        self.framePrincipal = tk.Frame(self.ventanaInicio, bg="black")
        self.framePrincipal.pack(fill="both", expand=True, padx=10)

        self.p1 = tk.Frame(self.framePrincipal, bg="dark blue")
        self.p1.pack(side="left", padx=10, fill="both", expand=True)

        self.p2 = tk.Frame(self.framePrincipal, bg="black")
        self.p2.pack(side="right", padx=10, fill="both", expand=True)

        #CREACION FRAME CV

        self.p2_label_frame = tk.Frame(self.p2, bg="white")
        self.p2_label_frame.pack(side="top", fill="both", expand=True)
        self.label_p2 = tk.Label(self.p2_label_frame, text=self.listaCv[0], font=("italic", 15), wraplength=270)
        self.label_p2.pack(pady=10)
        self.label_p2.bind("<Button-1>", lambda event: self.CV())
        self.p2_fotos_frame = tk.Frame(self.p2, bg="white")
        self.p2_fotos_frame.pack(pady=10)

        img = Image.open("src/1.gif")
        resized_img = img.resize((125, 150))
        pil = ImageTk.PhotoImage(resized_img)
        img2 = Image.open("src/2.gif")

        pil2 = ImageTk.PhotoImage(img2)
        img3 = Image.open("src/3.gif")

        pil3 = ImageTk.PhotoImage(img3)
        img4 = Image.open("src/4.gif")

        pil4 = ImageTk.PhotoImage(img4)

        self.label_p2_fotos = tk.Label(self.p2_fotos_frame, image=pil, )
        self.label_p2_fotos.grid(row=4, column=0, pady=5, padx=5, sticky="news")
        self.label_p3_fotos = tk.Label(self.p2_fotos_frame, image=pil, )
        self.label_p3_fotos.grid(row=3, column=0, pady=5, padx=5, sticky="news")
        self.label_p4_fotos = tk.Label(self.p2_fotos_frame, image=pil, )
        self.label_p4_fotos.grid(row=4, column=1, pady=5, padx=5, sticky="news")
        self.label_p5_fotos = tk.Label(self.p2_fotos_frame, image=pil, )
        self.label_p5_fotos.grid(row=3, column=1, pady=5, padx=5, sticky="news")

        #FRAME BIENVENIDA
        self.p3 = tk.Frame(self.p1, bg="light blue")
        self.p3.pack(side="top", padx=10, pady=10, fill="both", expand=True)
        self.label_p3 = tk.Label(self.p3, text="¡Bienvenido a Choopi!", font=("italic", 20))
        self.label_p3.pack(pady=10)

        self.p4 = tk.Frame(self.p1, bg="light blue")
        self.p4.pack(padx=10, pady=10, fill="both", expand=True)
        self.label_foto1 = tk.Label(self.p4)
        foto1 = Image.open("src/2.gif").resize((200, 356))
        foto1 = ImageTk.PhotoImage(foto1)
        self.label_foto1.config(image=foto1, compound="bottom")
        self.label_foto1.image = foto1  # Conservar una referencia para evitar el error
        self.label_foto1.pack(pady=10, padx=10)
        botonVentanaUsuario = tk.Button(self.p4, text="usuario interfaz", padx=10, pady=10, command=self.cambioDeVentana)
        botonVentanaUsuario.pack()

        self.ventanaPrincipalI = tk.Toplevel()
        self.ventanaPrincipalI.title("choopi")
        self.ventanaPrincipalI.geometry("600x500")

        self.menuP = tk.Menu(self.ventanaPrincipalI, tearoff=0)
        self.ventanaPrincipalI.config(menu=self.menuP)

        self.menuArchivo = tk.Menu(self.menuP, font=("italic"), tearoff=0)
        self.menuP.add_cascade(label="Archivo", menu=self.menuArchivo)
        self.menuArchivo.add_command(label="Aplicacion")
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Salir", command=self.volverVentana)

        self.MenuFuncionalidades = tk.Menu(self.menuP, font=("italic"), tearoff=0)
        self.menuP.add_cascade(label="Procesos y consultas", menu=self.MenuFuncionalidades)
        self.MenuFuncionalidades.add_command(label="Realizar Compra", command=lambda: self.cambiarContenido("Compra"))
        self.MenuFuncionalidades.add_command(label="Realizar Devolucion", command=lambda: self.cambiarContenido("Devolucion"))
        self.MenuFuncionalidades.add_command(label="Opinar", command=lambda: self.cambiarContenido("opinion"))
        self.MenuFuncionalidades.add_command(label="Estadistica", command=lambda: self.cambiarContenido("Estadistica"))

        self.frameContenedor = tk.Frame(self.ventanaPrincipalI, bg="blue")
        self.frameContenedor.pack(fill="both", expand=True)

        self.frameDelLabelDesc = tk.Frame(self.frameContenedor)
        self.frameDelLabelDesc.pack(pady=10)
        self.LabelDesc = tk.Label(self.frameDelLabelDesc, text="a", bg="white", font=("italic", 15), wraplength=270)
        self.LabelDesc.grid(row=0, column=0, columnspan=2)

        self.frameDelLabelDesc2 = tk.Frame(self.frameContenedor)
        self.frameDelLabelDesc2.pack(pady=10)
        self.LabelDesc2 = tk.Label(self.frameDelLabelDesc2, text="DESCRIPCION PROCESO O FUNCIONALIDAD", font=("italic", 15),
                                  wraplength=400)
        self.LabelDesc2.grid(row=2, column=0, columnspan=4)

        self.FrameWidgets = tk.Frame(self.frameContenedor, bg="white")
        self.FrameWidgets.pack(pady=10)
        self.cambiarContenido("Compra")

        self.ventanaPrincipalI.withdraw()
        self.ventana.mainloop()

app = Main()
