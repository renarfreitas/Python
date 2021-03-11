#O que são as Tuplas em Python - Curso de Python #15

#l_carros=["HRV","Golf","Argo"] # lista
t_carros=("HRV","Golf","Argo") # É sempre definida entre parenteses, Tuplas nao pode ser alterada diretamente.

l_carros=list(t_carros)
l_carros[2]="Focus"
t_carros=tuple(l_carros)

#print(t_carros[0])

for x in t_carros:
    print(x)
