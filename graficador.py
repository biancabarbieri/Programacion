import tkinter as tk  
from urllib.request import urlopen
from PIL import Image, ImageTk  
from io import BytesIO  

def descargarFondo():
    urlImagen = "https://github.com/biancabarbieri/proyectos/blob/main/1.png?raw=true"
    datosImagen = urlopen(urlImagen) 
    imagenBinaria = datosImagen.read()
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen


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
    label = tk.Label(ventana, text="Graficar la función", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def encontrarRaices():
    limpiarVentana()
    label = tk.Label(ventana, text="Graficar puntos específicos sobre la función", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def salirDelPrograma():
    limpiarVentana()
    label = tk.Label(ventana, text="Salir del programa", font=("Arial", 16))
    label.pack(pady=20)


def mostrarMenu():
    limpiarVentana()
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Graficar la función", font=("Arial", 14), width=20, command=graficarFuncion)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Graficar puntos específicos de la función", font=("Arial", 14), width=20, command=graficarPuntos)
    boton2.pack(pady=10)

    boton3 = tk.Button(ventana, text="Esncontrar raíces aproximadas a la función", font=("Arial", 14), width=20, command=encontrarRaices)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Salir del programa", font=("Arial", 14), width=20, command=salirDelPrograma)
    boton4.pack(pady=10)


def limpiarVentana():  
    for widget in ventana.winfo_children():  
        widget.destroy()

def main():
    global ventana
    ventana = tk.Tk()
    ventana.title("graficador")

    ancho = ventana.winfo_screenwidth()  
    alto = ventana.winfo_screenheight()  
    ventana.geometry(f"{ancho}x{alto}")

    imagen= descargarFondo()

    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

    imagenTk = ImageTk.PhotoImage(imagenRedimensionada)

    etiqueta = tk.Label(ventana, image=imagenTk)
    etiqueta.pack()  


    mostrarMenu()
    ventana.mainloop()

   


if __name__=="__main__":
    main()
