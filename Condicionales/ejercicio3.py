"""Escribir un programa que pida al usuario dos números y 
muestre por pantalla su división. Si el divisor es cero 
el programa debe mostrar un error."""

print("Division")
dividendo = int(input("Ingreso dividendo: "))
divisor = int(input("Ingrese divisor: "))

if divisor == 0:
    print("No se puede dividir por Cero")
else:
    division = dividendo / divisor
    print("El resultado es: " + str(round(division,2)))