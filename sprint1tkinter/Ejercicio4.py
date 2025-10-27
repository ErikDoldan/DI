import tkinter as tk


def actualizar():
    aficiones_seleccionadas = []

    if var_leer.get():
        aficiones_seleccionadas.append("Leer")
    if var_deporte.get():
        aficiones_seleccionadas.append("Deporte")
    if var_musica.get():
        aficiones_seleccionadas.append("Música")

    if aficiones_seleccionadas:
        estado = "Aficiones seleccionadas: " + ", ".join(aficiones_seleccionadas)
    else:
        estado = "No hay aficiones seleccionadas"

    etiqueta.config(text=estado)


root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")
root.geometry("400x250")

titulo = tk.Label(root, text="Selecciona tus aficiones:")
titulo.pack(pady=10)

var_leer = tk.IntVar()
var_deporte = tk.IntVar()
var_musica = tk.IntVar()

check_leer = tk.Checkbutton(root, text="Leer", variable=var_leer,command=actualizar)
check_leer.pack(pady=5)

check_deporte = tk.Checkbutton(root, text="Deporte", variable=var_deporte,command=actualizar)
check_deporte.pack(pady=5)

check_musica = tk.Checkbutton(root, text="Música", variable=var_musica,command=actualizar)
check_musica.pack(pady=5)

etiqueta= tk.Label(root, text="No hay aficiones seleccionadas")
etiqueta.pack(pady=10)

root.mainloop()