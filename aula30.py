# Jogo da Velha em Python - CFB Cusos Aula 30
import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
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
# Em construção...
while True:
    tela()
    #jog
    #cpu
    #vitoria
        try:
            break

