import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Has presionado el botón de mensaje!")

root = tk.Tk()
root.title("Ejercicio 2 - Button")
root.geometry("400x200")

etiqueta = tk.Label(root, text="Presiona un botón para ver el resultado")
etiqueta.pack(pady=20)

boton_mensaje = tk.Button(root, text="Mostrar Mensaje", command=mostrar_mensaje,bg="blue", fg="white")

boton_mensaje.pack(pady=10)

boton_salir = tk.Button(root, text="Cerrar Ventana", command=root.quit,bg="red", fg="white")
boton_salir.pack(pady=10)

root.mainloop()