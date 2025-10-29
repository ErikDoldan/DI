import tkinter as tk
from tkinter import messagebox


class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 12 - Registro de Usuarios")

        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menu_archivo.add_command(label="Salir", command=self.root.quit)

        tk.Label(self.root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        tk.Label(self.root, text="Edad:").pack()
        self.scale_edad = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.actualizar_edad)
        self.scale_edad.pack()

        self.etiqueta_edad = tk.Label(self.root, text="0 años")
        self.etiqueta_edad.pack()

        tk.Label(self.root, text="Género:").pack()
        self.var_genero = tk.StringVar()

        tk.Radiobutton(self.root, text="Masculino", variable=self.var_genero, value="Masculino").pack()
        tk.Radiobutton(self.root, text="Femenino", variable=self.var_genero, value="Femenino").pack()
        tk.Radiobutton(self.root, text="Otro", variable=self.var_genero, value="Otro").pack()

        tk.Button(self.root, text="Añadir", command=self.anadir_usuario).pack()

        tk.Label(self.root, text="Usuarios:").pack()

        frame = tk.Frame(self.root)
        frame.pack()

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT)

        scrollbar.config(command=self.listbox.yview)

        tk.Button(self.root, text="Eliminar", command=self.eliminar_usuario).pack()
        tk.Button(self.root, text="Salir", command=self.root.quit).pack()

        self.root.geometry("400x500")

    def actualizar_edad(self, valor):
        self.etiqueta_edad.config(text=f"{int(float(valor))} años")

    def anadir_usuario(self):
        nombre = self.entry_nombre.get()
        edad = int(self.scale_edad.get())
        genero = self.var_genero.get()

        if nombre and genero:
            usuario = f"{nombre} - {edad} años - {genero}"
            self.listbox.insert(tk.END, usuario)
            self.entry_nombre.delete(0, tk.END)
            self.scale_edad.set(0)
            self.var_genero.set("")

    def eliminar_usuario(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion[0])

    def guardar_lista(self):
        messagebox.showinfo("Guardar", "Lista guardada")

    def cargar_lista(self):
        messagebox.showinfo("Cargar", "Lista cargada")


root = tk.Tk()
app = RegistroApp(root)
root.mainloop()