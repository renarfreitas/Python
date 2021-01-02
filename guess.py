print("Welcome!") ##Exibe uma mensagem de boas vindas.
g = input("Guess the number: ") ## Pede ao usuário para fornecer ma adivinhação
guess = int(g) ##Converte a entrada em um número.
if guess == 5: ##O número advinhado era igual a 5?
    print("You win!") ##Informa ao usuário (Você venceu!)
else: ##Do contrário.
    print("You lose!") ##Informa ao usuário (Você perdeu!)
print("Game Over!") ##Fim de jogo. (Termina o programa)
