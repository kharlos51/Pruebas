import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi Programa")


def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir fichero")
    print(rutafichero)

boton = tkinter.Button(raiz, text="Pulsa para empezar", command=abrirfichero)
boton.pack()

raiz.mainloop()