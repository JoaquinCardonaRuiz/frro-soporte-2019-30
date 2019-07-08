## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 
import tkinter as tk
from tkinter import ttk
from functools import partial
import base64
print(str(base64.b64decode(b'Sm9hcXVpbiBDYXJkb25hIC0gR3J1cG8gMzA='))[2:-1])


root = tk.Tk()
tree=ttk.Treeview(root)
tree["columns"]=("one")
tree.column("#0", width=270, minwidth=270)
tree.column("#1", width=150, minwidth=150)
tree.heading("#0",text="Ciudad",anchor=tk.W)
tree.heading("#1", text="Codigo Postal",anchor=tk.W)

tree.insert("", 2, "1", text="Rosario", values=("2000"))
tree.insert("", 2, "2", text="Cordoba", values=("5000"))
tree.insert("", 2, "3", text="Mendoza", values=("5500"))
tree.insert("", 2, "4", text="Ushuaia", values=("9410"))
tree.insert("", 2, "5", text="Resistencia", values=("3500"))
tree.pack(side=tk.TOP,fill=tk.X)
root.title("Ciudades - ej03 - Grupo 30")
root.mainloop()

