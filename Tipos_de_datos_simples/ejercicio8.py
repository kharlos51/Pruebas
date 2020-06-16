"""Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un 
resto <r> donde <n> y <m> son los números introducidos por el 
usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""

n = input("Introduce el dividendo (numero entero): ")
m = input("Introduce el divisor (numero entero): ")

cociente = int(n) // int(m)
resto = int(n) % int(m)

print(n + " entre " + m + " da un cociente " + str(cociente) + " y un resto " + str(resto))