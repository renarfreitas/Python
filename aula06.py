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

frase = str(input(("Qual frase você deseja analisar: ?")))

l = []

for i in frase:
    if i not in l:
        l.append(i)
    print(i)
string = l
string_Invertida = string[::-1]
print("Sua palavra tem {} letras!".format(len(l)))
print(l)
print("Sua palavra invertida é: {}".format(string_Invertida))
nua = str(string_Invertida)
nua1 = nua.replace(",", "")
nua2 = nua1.replace("'", "")
nua3 = nua2.replace(" ", "")
print (str(nua3))