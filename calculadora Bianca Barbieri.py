import tkinter as tk

def suma():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    resultado=float
    num1 = float(input ("Ingrese el primer número"))
    num2 = float(input ("Ingrese el segundo número"))


    resultado = num1+ num2

    print (resultado)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def resta():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    resultado=float
    num1 = float(input ("Ingrese el primer número"))
    num2 = float(input ("Ingrese el segundo número"))


    resultado = num1- num2

    print (resultado)


    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def multiplicacion():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    resultado=float
    num1 = float(input ("Ingrese el primer número"))
    num2 = float(input ("Ingrese el segundo número"))


    resultado = num1* num2

    print (resultado)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def division():
    limpiarVentana()
    label = tk.Label(ventana, text="Ingrese ", font=("Arial", 16))
    label.pack(pady=20)

    resultado=float
    num1 = float(input ("Ingrese el primer número"))
    num2 = float(input ("Ingrese el segundo número"))


    resultado = num1/ num2

    print (resultado)

    
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarmenu)
    boton_volver.pack(pady=10)


def mostrarMenu():
    limpiarVentana()
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Realizar una suma", font=("Arial", 14), width=20, command=suma)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Realizar una resta", font=("Arial", 14), width=20, command=resta)
    boton2.pack(pady=10)

    boton3 = tk.Button(ventana, text="Realizar una multiplicación", font=("Arial", 14), width=20, command=multiplicacion)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Realizar una división", font=("Arial", 14), width=20, command=division)
    boton4.pack(pady=10)


def limpiarVentana():  
    for widget in ventana.winfo_children():  
        widget.destroy()

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("400x300")
    ventana.title("Calculadora")

    
    mostrarMenu()
    ventana.mainloop()





if __name__=="__main__":
    main()
