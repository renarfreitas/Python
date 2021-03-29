# Jogo da Velha em Python - CFB Cusos Aula 30
import os
import random
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
    print("0:  " + velha[0][0] + " | " + velha[0][0] + " | " )
    print("   -----------")
    print("1:  " + velha[0][0] + " | " + velha[0][0] + " | " )
    print("   -----------")
    print("2:  " + velha[0][0] + " | " + velha[0][0] + " | " )
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
        velha[l][c] = "0"
        jogadas += 1
        quemJoga = 2

while True:
    tela()
    jogadorJoga()
    cpuJoga()
    # Em construção...
    #vitoria
        try:
            break

