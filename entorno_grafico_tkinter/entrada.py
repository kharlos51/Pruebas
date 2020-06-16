import tkinter

raiz = tkinter.Tk()
raiz.title("Mi Programa")

entrada = tkinter.Entry(raiz)
entrada.config(justify="center",show="*")#show="*" esto para que muestre solo asteriscos
entrada.pack()

raiz.mainloop()