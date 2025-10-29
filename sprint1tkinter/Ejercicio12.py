import tkinter as tk
from tkinter import messagebox


def actualizar_edad(valor):
    etiqueta_edad.config(text=f"{int(float(valor))} años")


def anadir_usuario():
    nombre = entry_nombre.get()
    edad = int(scale_edad.get())
    genero = var_genero.get()

    if nombre and genero:
        usuario = f"{nombre} - {edad} años - {genero}"
        listbox.insert(tk.END, usuario)
        entry_nombre.delete(0, tk.END)
        scale_edad.set(0)
        var_genero.set("")


def eliminar_usuario():
    seleccion = listbox.curselection()
    if seleccion:
        listbox.delete(seleccion[0])


def guardar_lista():
    messagebox.showinfo("Guardar", "Lista guardada")


def cargar_lista():
    messagebox.showinfo("Cargar", "Lista cargada")


root = tk.Tk()
root.title("Ejercicio 12 - Registro de Usuarios")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_command(label="Salir", command=root.quit)

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
scale_edad = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=actualizar_edad)
scale_edad.pack()

etiqueta_edad = tk.Label(root, text="0 años")
etiqueta_edad.pack()

tk.Label(root, text="Género:").pack()
var_genero = tk.StringVar()

tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro").pack()

tk.Button(root, text="Añadir", command=anadir_usuario).pack()

tk.Label(root, text="Usuarios:").pack()

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)

tk.Button(root, text="Eliminar", command=eliminar_usuario).pack()
tk.Button(root, text="Salir", command=root.quit).pack()

root.geometry("400x500")
root.mainloop()