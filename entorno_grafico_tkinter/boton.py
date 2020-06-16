import tkinter

raiz = tkinter.Tk()
raiz.title("Mi Programa")

def accion():
    print("Hola Mundo")


boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()


raiz.mainloop()