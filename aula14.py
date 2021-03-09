#Loop While - Curso de Python #14
#Inicialização de Variável de controle
import os

i = 0
carros=[]
carro=input("Digite o nome do novo carro: ")
while carro != '-1':
  carros.append(carro)
  carro=input("Digite o nome do novo carro: ")

os.system('cls') #limpar a tela.
for x in carros:
  print(x)

print("Fim do Loop!")