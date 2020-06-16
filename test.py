import math

cards = 52

res = math.factorial(cards)
#print(res)

#print(len(str(res)))

i = 1
resultado = 1
while i <= cards:
    resultado = resultado * i
    print(resultado)
    i += 1


print(" ")
print(res)
