import tkinter as tk

def mostrar_contenido():
    contenido = entry.get()
    etiqueta_resultado.config(text=contenido)

def borrar_contenido():
    entry.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio 8 - Frame")
root.geometry("400x200")

frame_superior = tk.Frame(root)
frame_superior.pack()

tk.Label(frame_superior, text="Etiqueta 1").grid(row=0, column=0)
tk.Label(frame_superior, text="Etiqueta 2").grid(row=1, column=0)

entry = tk.Entry(frame_superior)
entry.grid(row=2, column=0)

etiqueta_resultado = tk.Label(frame_superior, text="")
etiqueta_resultado.grid(row=3, column=0)

frame_inferior = tk.Frame(root)
frame_inferior.pack()

tk.Button(frame_inferior, text="Mostrar", command=mostrar_contenido).grid(row=0, column=0)
tk.Button(frame_inferior, text="Borrar", command=borrar_contenido).grid(row=0, column=1)

root.mainloop()