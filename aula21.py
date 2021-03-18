#Funções P3 / Retorno de valores - Curso de Python #21
valores = [1,2,3,4,5,10,4,8]

def somar(num): #Argumentos arbritários
    r = 0
    for n in num:
        r+=n
    return r
def valLIsta(num):
    for v in num:
        print(v)
valLIsta(valores)
print(str(valores) + ": soma = " + str(somar(valores)))