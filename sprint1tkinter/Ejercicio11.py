import tkinter as tk

def actualizar_valor(valor):
    etiqueta_valor.config(text=f"Valor: {int(float(valor))}")

root = tk.Tk()
root.title("Ejercicio 11 - Scale")
root.geometry("400x200")

tk.Label(root, text="Selecciona un valor entre 0 y 100").pack()

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=actualizar_valor)
scale.pack()

etiqueta_valor = tk.Label(root, text="Valor: 0")
etiqueta_valor.pack()

root.mainloop()