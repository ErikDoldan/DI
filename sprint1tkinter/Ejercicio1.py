import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="¡El texto ha sido cambiado!")

root = tk.Tk()
root.title("Ejercicio 1 - Label")
root.geometry("400x200")

etiqueta1 = tk.Label(root, text="¡Bienvenido!")
etiqueta1.pack(pady=10)

etiqueta2 = tk.Label(root, text="Nombre: Erik Doldan Iglesias")
etiqueta2.pack(pady=10)

etiqueta3 = tk.Label(root, text="Este texto cambiará al pulsar el botón")
etiqueta3.pack(pady=10)

boton = tk.Button(root, text="Cambiar Texto", command=cambiar_texto,bg="green", fg="white")
boton.pack(pady=20)

root.mainloop()