## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 
import tkinter as tk
from tkinter import ttk
from functools import partial
import base64
print(str(base64.b64decode(b'Sm9hcXVpbiBDYXJkb25hIC0gR3J1cG8gMzA='))[2:-1])


def add(sv1="",sv2=""):
    global c
    def addcity():
        global c
        c+=1
        tree.insert("",2,str(c),text=n.get(),values=(cp.get()))
    addwin = tk.Toplevel()
    vp = tk.Frame(addwin)
    vp.grid(column=0,row=0,padx=(50,50),pady=(0,0))
    n,cp = tk.StringVar(),tk.StringVar()
    n.set(sv1)
    cp.set(sv2)
    b = tk.Button(vp,text="Aceptar",command=addcity)
    l1 = tk.Label(vp,text="Ciudad:")
    l2 = tk.Label(vp,text="CP:")
    e1 = tk.Entry(vp, textvariable = n)
    e2 = tk.Entry(vp, textvariable = cp)
    e1.grid(column=2,row=1)
    e2.grid(column=2,row=2)
    l1.grid(column=1,row=1)
    l2.grid(column=1,row=2)
    b.grid(column=1,row=3)

def mod():
    sel = tree.selection()[0]
    vals = tree.item(sel)
    add(sv1=vals["text"],sv2=vals["values"])
    tree.delete(sel)

def dl():
    sel = tree.selection()[0]
    tree.delete(sel)

root = tk.Tk()
tree=ttk.Treeview(root)
tree["columns"]=("one")
tree.column("#0", width=270, minwidth=270)
tree.column("#1", width=150, minwidth=150)
tree.heading("#0",text="Ciudad",anchor=tk.W)
tree.heading("#1", text="Codigo Postal",anchor=tk.W)
c=5
tree.insert("", 2, "1", text="Rosario", values=("2000"))
tree.insert("", 2, "2", text="Cordoba", values=("5000"))
tree.insert("", 2, "3", text="Mendoza", values=("5500"))
tree.insert("", 2, "4", text="Ushuaia", values=("9410"))
tree.insert("", 2, "5", text="Resistencia", values=("3500"))
tree.pack(side=tk.TOP,fill=tk.X)

badd = tk.Button(root,text="Alta",command=add)
bmod = tk.Button(root,text="Modificacion",command=mod)
bdel = tk.Button(root,text="Baja",command=dl)
badd.pack()
bmod.pack()
bdel.pack()

root.title("Ciudades - ej03 - Grupo 30")
root.mainloop()
