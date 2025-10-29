import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10 - Scrollbar")

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

texto = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
texto.pack(side=tk.LEFT)

scrollbar.config(command=texto.yview)

texto_largo = """fñlksdfñlskfñskfñskdñslkfdkfñdsmfñdsmfñdsmvñksmdvñkdsvmñdmvsdvds
msñkvmsñvmskdmvsñvmdñkmvskvmñsv
sñkvmdsñkvmdsñvmdsñkvmñskvmñdskvmñskdvmñskvms
vmsmvñksmñvmdskñvmsñvkvmsñdkvmñsdkvsmdvñskdvmñdskvmsdvmdsñmv
vsñkmvdñksvmñskvmdsñkvmdsñkvmdsñvmñsvm
vsmñvmdsñkvmsñkvmsñkvmsñdkvmvñksmvñkdsmvñdsvmdvds
ñvmñskvmñsvmñdsvmsdmvñskdmvñkdvdmvs
vñ


smvñvñdskvmñksdv
svdsv
ñsv
smvñkdsmvñkdsmvñskvmñskvm
v
smvñs
vm
ñksdmvñ
smñ
kmñvksvmsñdkvmñsvm
ñdsvñ
svm
ñsñvmvñsmv
ñsvñ
svm
ñdsvm
ñsvmñdskvmñdskvmsñ
vmsvñ
svsv
sñvñkñkmsñkvmdsks
mñkvsñkvmsvms
ñkñkvmmñksvñkmkvmñssvkmvñkmmñkv
ñvmsmñkvskvmdsñkmvsvñkmdv
vvv
ñvñvsñkvs
ñssvds
vdsñvs
vsmd
ñvsd
"""

texto.insert(tk.END, texto_largo)

root.mainloop()