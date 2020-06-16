"""Escribir un programa que pida al usuario su peso (en kg) y 
estatura (en metros), calcule el índice de masa corporal y lo 
almacene en una variable, y muestre por pantalla la frase 
Tu índice de masa corporal es <imc> donde <imc> es el índice de 
masa corporal calculado redondeado con dos decimales."""

print("Calcular Tu Indice de Masa Corporal")
peso = input("Ingresa tu peso en Kg: ")
estatura = input("Ingresa tu estatuta en Metros: ")
estatura_al_cuadrado = float(estatura)**2

imc = float(peso) / float(estatura_al_cuadrado)
imc_2 = round(imc,2) #para que muestre dos decimales

print("Tu indice de masa corporal es: " + str(imc_2))