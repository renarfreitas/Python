#Try Except / tratamento de erros - Curso de Python #26

try:
    print(x)
except NameError:
    print("X não está definido!")
except:
    print("Erro desconhecido!")

num = -10
if num < 1:
    raise Exception("Valor não permitido!")

try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento")

num = "Renar"

if not type(num) is int:
    raise Exception("Somente números permitidos")
else:
    print(num)