# Jogo da Velha em Python - CFB Cusos Aula 30
import os
import random
import colorama
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2 # 1 - CPU; 2 - Usuário
maxJogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogadas
    os.system("clear")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2] )
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2] )
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2] )
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
            while velha[l][c] != " ":
                l = int(input("Linha..:"))
                c = int(input("Coluna.:"))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e ou coluna invalida")
            
def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
        velha[l][c] = "O"
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
            ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "n"):
            break     
            il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "n"):
            break
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiag < 3:
            if (velha[idial][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if(soma == 3):
            vitoria = s
            break
    return vitoria

while True:
    tela()
    jogadorJoga()
    cpuJoga()

