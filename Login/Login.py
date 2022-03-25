from cProfile import label
from tkinter import *
from tkinter.ttk import *
from tokenize import String

index=Tk()
index.title("Inicio de sesion hecho por Eduardo")
index.config(bg="blue")
index.geometry("450x300")
index.resizable(width=False, height=False)

lusu=Label(index, width=14, text="Ingrese Usuario:", background="yellow")
lusu.pack()

user=StringVar()
eusu=Entry(index, width=30, textvariable=user, )
eusu.pack()

lpas=Label(index, width=18, text="Ingrese Contraseña:", background="yellow")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=30, show="*", textvariable=pas)
epas.pack()

def ingresar():
    if user.get()=="Eduardo" and pas.get()=="contra":
        index.title("Correcto")
    else:
     index.title("Incorrecto")

bl=Button (index, width=12, text="Iniciar sesion", command=ingresar)
bl.pack(side=BOTTOM)

index.mainloop()