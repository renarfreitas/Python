# Exercício Prático 1 Parte 1 e 2 - Curso de Python #27
import os

carros = []

class Carro:
    nome = ""
    potencia = 0
    velMax = 0
    ligado = False
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velMax = int(potencia)*2
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.desligar = False
    
    def info(self):
        print("Nome..............:" + self.nome)
        print("Potencia..........: " + self.potencia)
        print("Velocidade Máxima.:" + self.velMax)
        print("Ligado............:" + ("sim" if self.ligado == True else "não"))

def Menu():
    os.system("clear") or None
    print(" 1 - Novo Carro")
    print(" 2 - Informações do Carro")
    print(" 3 - Excluir Carro")
    print(" 4 - Ligar Carro")
    print(" 5 - Desligar Carro")
    print(" 6 - Listar Carro")
    print(" 7 - Sair")
    print(" * Quantidade de carros: " + str(len(carros)))
    opc = input("Digite uma opção: ")
    return opc

def NovoCarro():
    os.system("clear") or None
    n = input("Nome do Carro.....: ")
    p = input("Potencia do Carro.: ")
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro criado")

def informacoes():
    os.system("clear")
    n = int(input("Informe o numero do carro que deseja ver as informações: "))
    if n in carros:
        carros[n].info(n)
    else:
        print("Carro inexistente na lista!")

def excluircarro():
    os.system("clear")
    n = input("Informe o numero do carro que deseja excluir: ")
    try:
        del carros[int(n)]
    except:
        print("Carro inexistente na lista!")

def ligarCarro():
    os.system("clear")
    n = input("Informe o numero do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro ligado")
    except:
        print("Carro inexistente na lista!")

def desligarCarro():
    os.system("clear")
    n = input("Informe o numero do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("Carro inexistente na lista!")

def listarCarros():
    os.system("clear") or None
    p = 0
    for c in carros:
        print(str(p) + " - " + c.nome)
        p = p + 1

def retornarmenu():
    Menu()

ret = Menu()
while ret < "7":
    if ret == "1":
        NovoCarro()
    elif ret == "2":
        informacoes()
    elif ret == "3":
        excluircarro()
    elif ret == "4":
        ligarCarro()
    elif ret == "5":
        desligarCarro()
    elif ret == "6":
        listarCarros()
    ret = Menu()
os.system("clear") or None
print("Programa finalizado")