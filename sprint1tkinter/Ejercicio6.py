import tkinter as tk

def mostrar_seleccion():
    seleccion = listbox.curselection()
    if seleccion:
        fruta = listbox.get(seleccion[0])
        etiqueta_resultado.config(text=f"Has seleccionado: {fruta}")
    else:
        etiqueta_resultado.config(text="No has seleccionado ninguna fruta")

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")
root.geometry("400x300")

titulo = tk.Label(root, text="Selecciona una fruta:")
titulo.pack(pady=10)

listbox = tk.Listbox(root, height=5, width=20)
listbox.pack(pady=10)

frutas = ["Manzana", "Banana", "Naranja"]
for fruta in frutas:
    listbox.insert(tk.END, fruta)

boton = tk.Button(root, text="Mostrar Fruta Seleccionada",command=mostrar_seleccion, bg="#FF9800", fg="white")
boton.pack(pady=10)

etiqueta_resultado = tk.Label(root, text="",fg="blue")
etiqueta_resultado.pack(pady=10)

root.mainloop()