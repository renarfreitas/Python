#Matrizes - Curso de Python #16

carros = [
    ["Modelo", "HRV"],
    ["Fabricante","Honda"],
    ["Ano",2016]
] #Array / List

carros.append(["Cor","Prata"])

#carros[2][1] = 2019

for l, c in carros:
    print(l + " | " + str(c))