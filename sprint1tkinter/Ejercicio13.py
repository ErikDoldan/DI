import tkinter as tk

def dibujar_circulo(event):
    x = event.x
    y = event.y
    radio = 10
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio)

def limpiar_canvas(event):
    canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13 - Eventos")

tk.Label(root, text="Haz clic para dibujar círculos. Presiona 'c' para limpiar").pack()

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.bind("<Button-1>", dibujar_circulo)
root.bind("<c>", limpiar_canvas)

root.mainloop()