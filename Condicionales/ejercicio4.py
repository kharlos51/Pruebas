"""Para tributar un determinado impuesto se debe ser mayor 
de 16 años y tener unos ingresos iguales o superiores 
a 1000 € mensuales. Escribir un programa que pregunte al 
usuario su edad y sus ingresos mensuales y muestre por 
pantalla si el usuario tiene que tributar o no."""

edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese el total de sus ingresos mensuales: "))

if edad >= 17:
    if ingresos >= 1000:
        print("Debes tributar")
    else:
        print("No debes tributar")
else:
    print("No debes tributar")
