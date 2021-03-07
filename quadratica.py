import math

print("Informe 3 valores:")
a = float(input("Valor a: "))
b = float(input("Valor b: "))
c = float(input("Valor c: "))

delta = b ** 2 - 4 * a * c
#Aplicando Bhaskara:
"""
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

if delta == 0:
    print("A unica raiz é: {}".format(x1))
if delta > 0:
    print("O valor de Delta é {}".format(delta))
    print("Delta tem duas raízes reais que são: {",x1,",",x2,"}")
else:
    if delta < 0:
        print("Para esta equação não exite raízes reais")
"""
if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A unica raiz é: {}".format(x1))
else:
    if delta < 0:
        print("Para esta equação não exite raízes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Delta tem duas raízes reais que são: {",x1,",",x2,"}")