"""Escribir un programa que pregunte al usuario una cantidad a 
invertir, el interés anual y el número de años, y muestre por 
pantalla el capital obtenido en la inversión."""

cantidad = float(input("Intruduce cantidad a invertir: "))
interes = float(input("Introduce interes anual: "))
anios = int(input("Intruduce cantidad de años: "))

capital_final = round(cantidad * (interes / 100 +1) ** anios, 2)

print(str(capital_final))