"""Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la contraseña 
e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

contra = "carlitox"
passw = input("Introdusca su contraseña: ")
password = passw.lower()

if contra == password:
    print("Contraseña Correcta")
else:
    print("Contraseña Incorrecta!")

