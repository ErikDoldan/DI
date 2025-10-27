import tkinter as tk

def mostrar_saludo():
    nombre = entrada.get()
    if nombre:
        etiqueta_saludo.config(text=f"¡Hola, {nombre}! Bienvenido/a")
    else:
        etiqueta_saludo.config(text="Por favor, introduce tu nombre")

root = tk.Tk()
root.title("Ejercicio 3 - Entry")
root.geometry("400x200")

etiqueta_instruccion = tk.Label(root, text="Introduce tu nombre:")
etiqueta_instruccion.pack(pady=10)

entrada = tk.Entry(root, width=30)
entrada.pack(pady=5)

boton = tk.Button(root, text="Saludar", command=mostrar_saludo)
boton.pack(pady=10)

etiqueta_saludo = tk.Label(root, text="")
etiqueta_saludo.pack(pady=10)
root.mainloop()