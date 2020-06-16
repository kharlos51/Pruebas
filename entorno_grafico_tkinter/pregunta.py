import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi Programa")

def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo Pregunta", "¿Quieres borrar el fichero?")
    if (resultado == "yes"):
        print("Si, quiero borrar el fichero")
    else:
        print("No, no quiero borrar el fichero")

boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
boton.pack()

raiz.mainloop()