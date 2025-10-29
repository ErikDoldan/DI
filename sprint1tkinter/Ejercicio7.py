import tkinter as tk

def dibujar_rectangulo():
    x1 = int(entry_rect_x1.get())
    y1 = int(entry_rect_y1.get())
    x2 = int(entry_rect_x2.get())
    y2 = int(entry_rect_y2.get())
    canvas.create_rectangle(x1, y1, x2, y2)

def dibujar_circulo():
    x1 = int(entry_circ_x1.get())
    y1 = int(entry_circ_y1.get())
    x2 = int(entry_circ_x2.get())
    y2 = int(entry_circ_y2.get())
    canvas.create_oval(x1, y1, x2, y2)

root = tk.Tk()
root.title("Ejercicio 7 - Canvas")

tk.Label(root, text="Rectángulo:").pack()
tk.Label(root, text="x1:").pack()
entry_rect_x1 = tk.Entry(root)
entry_rect_x1.pack()

tk.Label(root, text="y1:").pack()
entry_rect_y1 = tk.Entry(root)
entry_rect_y1.pack()

tk.Label(root, text="x2:").pack()
entry_rect_x2 = tk.Entry(root)
entry_rect_x2.pack()

tk.Label(root, text="y2:").pack()
entry_rect_y2 = tk.Entry(root)
entry_rect_y2.pack()

tk.Button(root, text="Dibujar Rectángulo", command=dibujar_rectangulo).pack()

tk.Label(root, text="Círculo:").pack()
tk.Label(root, text="x1:").pack()
entry_circ_x1 = tk.Entry(root)
entry_circ_x1.pack()

tk.Label(root, text="y1:").pack()
entry_circ_y1 = tk.Entry(root)
entry_circ_y1.pack()

tk.Label(root, text="x2:").pack()
entry_circ_x2 = tk.Entry(root)
entry_circ_x2.pack()

tk.Label(root, text="y2:").pack()
entry_circ_y2 = tk.Entry(root)
entry_circ_y2.pack()

tk.Button(root, text="Dibujar Círculo", command=dibujar_circulo).pack()

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

root.mainloop()
