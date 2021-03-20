#Funções Lamda ou Funções Anônimas - Curso de Python #22
#Forma 1
soma = lambda a,b:a+b
#Forma 2
num = lambda a, b, c: (a+b)*c
print(soma(2,5))
print(num(2,5,3))
#Forma 3
print((lambda a, b : a+b)(3,2))

r = lambda x, func:x+func(x)
res=r(2,lambda x:x*x)

print(res)