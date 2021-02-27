#Strings P1 - Curso de Python #06
curso = "Curso de Python"

print(curso)
print("Tamanho: " + str(len(curso)))
#Função para remover espaços
print(curso.strip())
#Função que converte para minusculos
print(curso.lower())
#Função que converte em maiusculos
print(curso.upper())
#Função que substitui uma string ou caracter
print(curso.replace("Python", "Py#"))
#Função que subdivide a string por indicador escolhido
a = curso.split(" ")
print(a[0])
print(a[1])
print(a[2])
