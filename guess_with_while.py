from random import randint
secret = randint (1,10)#A variavel secret será definida para um número aleatório entre 1 e 10.
print("Welcome!") #Exibe uma mensagem de boas vindas.#

guess = 0 
while guess != secret:
    g = input("Guess the number: ") #Pede ao usuário para fornecer ma adivinhação#
    guess = int(g) #Converte a entrada em um número.#
    if guess == secret: #O número adivinhado era igual a 5?#
        print("You win!") #Informa ao usuário (Você venceu!)#
    else:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
#print("You lose!") #Informa ao usuário (Você perdeu!)#
print("Game Over!") #Fim de jogo. (Termina o programa)#
