## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
import base64
print(str(base64.b64decode(b'Sm9hcXVpbiBDYXJkb25hIC0gR3J1cG8gMzA='))[2:-1])

def add():
    try:
        result = str(float(v1.get()) + float(v2.get()))
    except:
        result = "Valores invalidos"
    r.set(result)

def sub():
    try:
        result = str(float(v1.get()) - float(v2.get()))
    except:
        result = "Valores invalidos"
    r.set(result)

def mul():
    try:
        result = str(float(v1.get()) * float(v2.get()))
    except:
        result = "Valores invalidos"
    r.set(result)

def div():
    try:
        result = str(float(v1.get()) / float(v2.get()))
    except:
        result = "Valores invalidos"
    r.set(result)

import tkinter as tk
root = tk.Tk()
vp = tk.Frame(root)
vp.grid(column=0,row=0,padx=(50,50),pady=(0,0))
l1,l2,l3 = [tk.Label(vp,text=i) for i in ["Valor 1","Valor 2","Resultado"]]
b1,b2,b3,b4 = [tk.Button(vp,text=i, command=j) for i,j in zip(["+","-","*","/"],[add,sub,mul,div])]
v1,v2,r = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
e1,e2,e3 = [tk.Entry(vp,textvariable = i) for i in(v1,v2,r)]
l1.grid(column=1,row=1)
l2.grid(column=2,row=1)
l3.grid(column=3,row=1)
e1.grid(column=1,row=2)
e2.grid(column=2,row=2)
e3.grid(column=3,row=2)
b1.grid(column=2,row=3)
b2.grid(column=2,row=4)
b3.grid(column=2,row=5)
b4.grid(column=2,row=6)
root.title("Calculadora - ej01 - Grupo 30")
root.mainloop()

