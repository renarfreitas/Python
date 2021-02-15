import os

nome = "teste.txt"
f = open("C://Python36-32//Aula//"+nome,"wt")
for l in os.popen('systeminfo'):
    conj = (l.rstrip)
    print (conj)
f.close()
