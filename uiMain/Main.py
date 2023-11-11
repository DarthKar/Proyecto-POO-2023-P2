import tkinter as tk

ventana = tk.Tk()
ventana.title("Choope")
ventana.geometry("600x600")

ventanaInicio = tk.Frame(ventana)
ventanaInicio.pack(fill="both", expand=True)

menuInicio = tk.Menu(ventana)
ventana.config(menu=menuInicio)

menu1 = tk.Menu(menuInicio, font=("italic", 16))
menuInicio.add_cascade(label="Inicio", menu=menu1)

p1 = tk.Frame(ventanaInicio, bg="red")
p1.pack(fill="both", expand=True, padx=10)

p2 = tk.Frame(p1, bg="blue")
p2.pack(side="left", padx=10, fill="y")

p3 = tk.Frame(p2, bg="green")
p3.pack(side="top", padx=10, pady=10)
label_p3 = tk.Label(p3, text="¡Bienvenido a Choope!", font=("italic", 16))
label_p3.pack(pady=10)

p4 = tk.Frame(p2, bg="green")
p4.pack(padx=10, pady=10)
label_foto1 = tk.Label(p4, padx=10, pady=10)
foto1 = tk.PhotoImage(file="src\image1.png")
label_foto1.config(image=foto1,compound="bottom")
label_foto1.pack(pady=10)
botonVentanaUsuario= tk.Button(p4,text="Usuario interfaz", padx=10,pady=10)
botonVentanaUsuario.pack()



ventana.mainloop()
