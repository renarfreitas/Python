import os

nome = "teste.txt"
f = open("C://Python36-32//Aula//"+nome,"wt")

for l in os.popen('systeminfo'):
    informacao = (l.rstrip())
    f.write(informacao)
    print (informacao)
f.close()
