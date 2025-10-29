import tkinter as tk
from tkinter import messagebox

def abrir_archivo():
    messagebox.showinfo("Abrir", "Abrir archivo")

def salir_aplicacion():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación de ejemplo\nVersión 1.0")

root = tk.Tk()
root.title("Ejercicio 9 - Menu")
root.geometry("400x200")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

tk.Label(root, text="Usa el menú superior").pack()

root.mainloop()