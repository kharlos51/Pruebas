"""Escribir un programa que pregunte el nombre del usuario en la 
consola y después de que el usuario lo introduzca muestre por 
pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de 
usuario en mayúsculas y <n> es el número de letras que tienen el nombre."""

nombre = input("Introduce un nombre: ")
numero_de_letras = str(len(nombre))
nombre_mayus = nombre.upper()

print("Tu nombre es: " + nombre_mayus + " y tiene " + numero_de_letras + " letras")