#Funções P2 / argumentos de entrada - Curso de Python #20
'''
n1 = 15
n2 = 7
def somar(n1, n2):
    r = n1 + n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))
    print("youtube.com/cfbcursos\n")
somar(5, 7)
somar(12, 8)

def textos(*txt):
    for t in txt:
        print(t)

textos("CFB Cursos",  "Python", "Canal", "Curso", "Computador")

'''
valores = [1,2,3,4,5]

def somar(num): #Argumentos arbritários
    r = 0
    for n in num:
        r+=n

    print("Soma = " + str(r))
    print("youtube.com/cfbcursos\n")
somar(valores)

def carros(c="Golf"):
    print("Modelo: " + c)
carros()