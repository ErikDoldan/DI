import tkinter as tk

def cambiar_color():
    color = var_color.get()
    root.config(bg=color)

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")
root.geometry("400x250")


titulo = tk.Label(root, text="Elige tu color favorito:")
titulo.pack(pady=10)

var_color = tk.StringVar()
var_color.set("white")

frame_radio = tk.Frame(root, bg="white")
frame_radio.pack(pady=10)

radio_rojo = tk.Radiobutton(frame_radio, text="Rojo", variable=var_color,value="red", command=cambiar_color)
radio_rojo.pack(pady=5)

radio_verde = tk.Radiobutton(frame_radio, text="Verde", variable=var_color,value="green", command=cambiar_color)
radio_verde.pack(pady=5)

radio_azul = tk.Radiobutton(frame_radio, text="Azul", variable=var_color, value="blue", command=cambiar_color)
radio_azul.pack(pady=5)

etiqueta_info = tk.Label(root, text="El fondo cambiará al color seleccionado")
etiqueta_info.pack(pady=10)

root.mainloop()