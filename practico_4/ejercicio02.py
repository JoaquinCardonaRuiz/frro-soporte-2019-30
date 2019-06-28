## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 
import tkinter as tk
from functools import partial
import base64
print(str(base64.b64decode(b'Sm9hcXVpbiBDYXJkb25hIC0gR3J1cG8gMzA='))[2:-1])



def agregar(arg):
    print("number pressed: "+ arg)
    if arg == "=":
        s.set(eval(s.get()))
    else:
        s.set(s.get()+arg)

root = tk.Tk()
vp = tk.Frame(root)
vp.grid(column=0,row=0,padx=(50,50),pady=(0,0))
b1,b2,b3,b4,b5,b6,b7,b8,b9,b0,badd,bsub,bmul,bdiv,beq = [tk.Button(vp,text = i, command = partial(agregar, i)) for i in ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","="]]
s = tk.StringVar()
e = tk.Entry(root,textvariable = s)
e.grid(column=1,row=1)
b1.grid(column=1,row=2)
b2.grid(column=2,row=2)
b3.grid(column=3,row=2)
b4.grid(column=1,row=3)
b5.grid(column=2,row=3)
b6.grid(column=3,row=3)
b7.grid(column=1,row=4)
b8.grid(column=2,row=4)
b9.grid(column=3,row=4)
b0.grid(column=1,row=5)
badd.grid(column=4,row=2)
bsub.grid(column=4,row=3)
bmul.grid(column=4,row=4)
bdiv.grid(column=4,row=5)
beq.grid(column=2,row=5)
root.title("Calculadora - ej02 - Grupo 30")
root.mainloop()

