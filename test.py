import os

nome = "teste.txt"
f = open("C:/Users/Sasaque/OneDrive/Área de Trabalho/"+nome,"wt")

for l in os.popen('systeminfo'):
    informacao = (l.rstrip())
    f.write(informacao)
f.close()


