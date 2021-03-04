#Como usar o comando IF em Python - Curso de Python #10

a = 10
b = 5
res = 0
op = "*"

if op == "+":
    res = a + b

if op == "-":
    res = a - b

if op == "*":
    res = a * b

if op == "/":
    res = a / b

print(str(a) + op + str(b) + " = " + str(res))