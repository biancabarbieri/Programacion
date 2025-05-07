import tkinter as tk  
from urllib.request import urlopen
from PIL import Image, ImageTk  
from io import BytesIO 

def descargarFondo():
    urlImagen = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/CABJ70.png/960px-CABJ70.png"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read()
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarFondo2():
    urlImagen2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/CABJ70.png/960px-CABJ70.png"
    datosImagen2 = urlopen(urlImagen2) 
    imagenBinaria2 = datosImagen2.read()
    imagen2 = Image.open(BytesIO(imagenBinaria2))
    return imagen2

def funcionPolinomica():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=graficarFuncion)
    boton_volver.pack(pady=10)

def funcionLogaritmica():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=graficarFuncion)
    boton_volver.pack(pady=10)

def funcionExponencial():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=graficarFuncion)
    boton_volver.pack(pady=10)


def graficarFuncion():
    limpiarVentana()
    label = tk.Label(ventana, text="graficar la función", font=("Arial", 16))
    label.pack(pady=20)
    label = tk.Label(ventana, text="Elija que función", font=("Arial", 16))
    label.pack(pady=20)
    boton1 = tk.Button(ventana, text="polinomica", font=("Arial", 12), command=funcionPolinomica)
    boton1.pack(pady=10)
    boton_volver = tk.Button(ventana, text="logaritmica", font=("Arial", 12), command=funcionLogaritmica)
    boton_volver.pack(pady=10)
    boton_volver = tk.Button(ventana, text="exponencial", font=("Arial", 12), command=funcionExponencial)
    boton_volver.pack(pady=10)
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def graficarPuntos():
    limpiarVentana()
    label = tk.Label(ventana, text="Graficar puntos específicos sobre la función")
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pac()

def encontrarRaices():
    limpiarVentana()
    label = tk.Label(ventana, text="Encontrar raíces aproximadas a la función", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def salirDelPrograma():
    limpiarVentana()
    label = tk.Label(ventana, text="Salir del programa", font=("Arial", 16))
    label.pack(pady=20)


def mostrarMenu():
    limpiarVentana()
    
   
    imagen= descargarFondo2()

    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

    imagenTk = ImageTk.PhotoImage(imagenRedimensionada)
    etiqueta = tk.Label(ventana, image=imagenTk)
    etiqueta.pack()

    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.place(x=350,y=500)

    boton1 = tk.Button(ventana, text="Graficar la función", font=("Arial", 14), width=20, command=graficarFuncion)
    boton1.place(x=600, y=300)

    boton2 = tk.Button(ventana, text="Graficar puntos específicos de la función", font=("Arial", 14), width=20, command=graficarPuntos)
    boton2.place(x=600, y=400)

    boton3 = tk.Button(ventana, text="Encontrar raíces aproximadas a la función", font=("Arial", 14), width=20, command=encontrarRaices)
    boton3.place(x=600, y=500)

    boton4 = tk.Button(ventana, text="Salir del programa", font=("Arial", 14), width=20, command=salirDelPrograma)
    boton4.place(x=600, y=600)
   
    


def limpiarVentana():  
    for widget in ventana.winfo_children():  
        widget.destroy()
    

def main():
    global ventana
    global imagen
    global alto
    global ancho
    
    ventana = tk.Tk()
    ventana.title("graficador")

    ancho = ventana.winfo_screenwidth()  
    alto = ventana.winfo_screenheight()  
    ventana.geometry(f"{ancho}x{alto}")

    imagen= descargarFondo()

    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

    imagenTk = ImageTk.PhotoImage(imagenRedimensionada)
    etiqueta = tk.Label(ventana, image=imagenTk)
    etiqueta.place(x=0,y=0,relwidth=1, relheight=1)
    
    boton_inicio = tk.Button(ventana, text="Mostrar menú", font=("Arial", 15), width=22, command=mostrarMenu)
    boton_inicio.place(x=600, y=300)
    
    ventana.mainloop()

if __name__=="__main__":
    main()
